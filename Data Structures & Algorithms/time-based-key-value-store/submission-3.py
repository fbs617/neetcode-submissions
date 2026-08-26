class TimeMap:

    def __init__(self):
        self.__tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.__tm[key] = self.__tm.get(key, [])
        self.__tm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.__tm:
            return ""
        vals = self.__tm[key]
        lo, hi = 0, len(vals) - 1
        largest_tm = -1
        out = ""
        while lo <= hi:
            mid = (lo+hi) // 2
            val_mid = vals[mid][0]
            if val_mid > timestamp:
                hi = mid - 1
            elif val_mid <= timestamp:
                if val_mid > largest_tm:
                    out = vals[mid][1]
                lo = mid + 1
        return out
        
