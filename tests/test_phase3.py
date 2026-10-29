import pytest
from verify.reconcile import verify_lot_split_math
from verify.feasibility import check_allocation_feasibility

def test_split_mass_balance_valid():
    res = verify_lot_split_math(
        parent_weight_g=985000,
        child_weights_g=[600000, 375000],
        loss_g=10000,
        reason=0
    )
    assert res["valid"] is True
    assert res["is_balanced"] is True
    assert res["loss_ok"] is True

def test_split_mass_balance_exceeds_parent():
    res = verify_lot_split_math(
        parent_weight_g=985000,
        child_weights_g=[600000, 500000],
        loss_g=0,
        reason=0
    )
    assert res["valid"] is False
    assert res["is_balanced"] is False

def test_split_loss_above_tolerance():
    res = verify_lot_split_math(
        parent_weight_g=985000,
        child_weights_g=[945000],
        loss_g=40000,
        reason=0
    )
    assert res["valid"] is False
    assert res["loss_ok"] is False

def test_feasibility_checker_valid_allocation():
    lots = [
        {"id": 1, "weight_g": 600000, "allocated_weight_g": 0, "grade": 3},
        {"id": 2, "weight_g": 385000, "allocated_weight_g": 0, "grade": 2},
    ]
    contract = {"id": 1, "min_grade": 2, "qty_g": 1000000}
    allocation = {1: 600000, 2: 385000}

    report = check_allocation_feasibility(lots, contract, allocation)
    assert report["feasible"] is True
    assert len(report["violations"]) == 0
    assert report["total_assigned_g"] == 985000

def test_feasibility_checker_rejects_over_capacity():
    lots = [
        {"id": 1, "weight_g": 700000, "allocated_weight_g": 0, "grade": 2},
        {"id": 2, "weight_g": 500000, "allocated_weight_g": 0, "grade": 2},
    ]
    contract = {"id": 1, "min_grade": 2, "qty_g": 1000000}
    allocation = {1: 700000, 2: 500000}

    report = check_allocation_feasibility(lots, contract, allocation)
    assert report["feasible"] is False
    assert any("exceeds contract capacity" in v for v in report["violations"])

def test_feasibility_checker_rejects_substandard_grade():
    lots = [
        {"id": 1, "weight_g": 500000, "allocated_weight_g": 0, "grade": 1},
    ]
    contract = {"id": 1, "min_grade": 2, "qty_g": 1000000}
    allocation = {1: 500000}

    report = check_allocation_feasibility(lots, contract, allocation)
    assert report["feasible"] is False
    assert any("below contract minimum" in v for v in report["violations"])
