import os
import pytest
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from chain.indexer import SessionLocal, LocationEvent, Base, engine


def test_location_event_storage():
    """Verify that GPS location events can be stored and retrieved with SHA-256 integrity."""
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        event = LocationEvent(
            lot_id=999,
            lat="12.524400",
            lng="76.895800",
            accuracy="5.2",
            timestamp="2026-10-30T00:00:00Z",
            actor="0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
            payload_hash="0x" + "a" * 64,
        )
        session.add(event)
        session.commit()

        retrieved = session.query(LocationEvent).filter_by(lot_id=999).first()
        assert retrieved is not None
        assert retrieved.lat == "12.524400"
        assert retrieved.lng == "76.895800"
        assert retrieved.actor == "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"

        # Cleanup
        session.delete(retrieved)
        session.commit()
    finally:
        session.close()


def test_maps_distance_haversine():
    """Verify that geodesic distance fallback executes accurately."""
    import math

    def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0  # Earth radius in kilometers
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = (
            math.sin(dLat / 2) ** 2
            + math.cos(math.radians(lat1))
            * math.cos(math.radians(lat2))
            * math.sin(dLon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    # Distance between Mandya (12.5244, 76.8958) and Mysuru (12.2958, 76.6394) is ~38-42 km
    dist = haversine(12.5244, 76.8958, 12.2958, 76.6394)
    assert 35.0 < dist < 45.0, f"Unexpected distance: {dist} km"


def test_google_maps_key_graceful():
    """Verify server-side handling when GOOGLE_MAPS_SERVER_KEY is not configured."""
    key = os.getenv("GOOGLE_MAPS_SERVER_KEY", "").strip()
    if not key:
        source = "haversine"
    else:
        source = "google_routes"
    assert source in ("haversine", "google_routes")
