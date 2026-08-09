class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        result = ""
        i, j = 0, len(self.timemap[key]) - 1
        while i <= j:
            m = (i+j) // 2
            if self.timemap[key][m][1] == timestamp:
                return self.timemap[key][m][0]
            elif self.timemap[key][m][1] < timestamp:
                result = self.timemap[key][m][0]
                i = m + 1
            else:
                j = m - 1

        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)