import { useState, useEffect, useCallback } from "react";
import { agroApi } from "../api.js";

const DB_NAME = "AgroTraceOfflineDB";
const STORE_NAME = "offline_actions";

function openDB() {
  return new Promise((resolve, reject) => {
    if (typeof indexedDB === "undefined") {
      resolve(null);
      return;
    }
    const request = indexedDB.open(DB_NAME, 1);
    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      if (!db.objectStoreNames.contains(STORE_NAME)) {
        db.createObjectStore(STORE_NAME, { keyPath: "id", autoIncrement: true });
      }
    };
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

export function useOfflineQueue() {
  const [isOnline, setIsOnline] = useState(
    typeof navigator !== "undefined" ? navigator.onLine : true
  );
  const [queueCount, setQueueCount] = useState(0);
  const [isSyncing, setIsSyncing] = useState(false);
  const [lastSyncResult, setLastSyncResult] = useState(null);

  const refreshCount = useCallback(async () => {
    try {
      const db = await openDB();
      if (!db) return;
      const tx = db.transaction(STORE_NAME, "readonly");
      const store = tx.objectStore(STORE_NAME);
      const countReq = store.count();
      countReq.onsuccess = () => setQueueCount(countReq.result);
    } catch {
      // IndexedDB optional error suppression
    }
  }, []);

  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);
    refreshCount();

    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, [refreshCount]);

  const enqueueAction = useCallback(
    async (type, payload) => {
      try {
        const db = await openDB();
        if (!db) return;
        const tx = db.transaction(STORE_NAME, "readwrite");
        const store = tx.objectStore(STORE_NAME);
        store.add({
          type,
          payload,
          timestamp: new Date().toISOString(),
        });
        tx.oncomplete = () => refreshCount();
      } catch (err) {
        console.warn("Offline action storage failed", err);
      }
    },
    [refreshCount]
  );

  const syncQueue = useCallback(async () => {
    if (isSyncing) return;
    setIsSyncing(true);
    try {
      const db = await openDB();
      if (!db) {
        setIsSyncing(false);
        return;
      }
      const tx = db.transaction(STORE_NAME, "readonly");
      const store = tx.objectStore(STORE_NAME);
      const req = store.getAll();

      req.onsuccess = async () => {
        const items = req.result || [];
        if (items.length === 0) {
          setIsSyncing(false);
          return;
        }

        const serializedRecords = items.map((item) =>
          JSON.stringify({
            type: item.type,
            payload: item.payload,
            timestamp: item.timestamp,
          })
        );

        try {
          const res = await agroApi.syncBatch(serializedRecords, true);
          setLastSyncResult(res);

          // Clear synchronized items
          const clearTx = db.transaction(STORE_NAME, "readwrite");
          clearTx.objectStore(STORE_NAME).clear();
          clearTx.oncomplete = () => {
            refreshCount();
            setIsSyncing(false);
          };
        } catch (syncErr) {
          console.error("Batch Merkle sync failed:", syncErr);
          setIsSyncing(false);
        }
      };
    } catch (e) {
      console.error("Error reading offline queue:", e);
      setIsSyncing(false);
    }
  }, [isSyncing, refreshCount]);

  return {
    isOnline,
    queueCount,
    isSyncing,
    lastSyncResult,
    enqueueAction,
    syncQueue,
  };
}
