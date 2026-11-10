'use client';

import { useState, useEffect, useCallback } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(initialValue);
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    try {
      const item = window.localStorage.getItem(key);
      if (item) {
        setStoredValue(JSON.parse(item));
      }
    } catch (error) {
      console.warn(`Lỗi đọc localStorage key "${key}":`, error);
    } finally {
      setIsReady(true);
    }
  }, [key]);

  const setValue = useCallback(
    (value: T | ((val: T) => T)) => {
      try {
        setStoredValue((prev) => {
          const valueToStore = value instanceof Function ? value(prev) : value;
          if (typeof window !== 'undefined') {
            try {
              window.localStorage.setItem(key, JSON.stringify(valueToStore));
            } catch (quotaErr) {
              console.warn(`LocalStorage quota exceeded khi lưu "${key}":`, quotaErr);
            }
          }
          return valueToStore;
        });
      } catch (error) {
        console.warn(`Lỗi cập nhật state cho "${key}":`, error);
      }
    },
    [key]
  );

  return [storedValue, setValue, isReady] as const;
}
