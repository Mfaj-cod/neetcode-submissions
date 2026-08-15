class LFUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(list)
        self.space = capacity

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache[key][1] += 1

        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.space > 0:
            self.cache[key] = [value, 1]
            self.space -= 1
            return
        elif key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
        elif key not in self.cache and self.space <= 0:
            lru = [0, float('inf')]
            for k, v in self.cache.items():
                if v[1] < lru[1]:
                    lru = [k, v[1]]
            self.cache.pop(lru[0], None)
            self.space += 1
            # inserting new
            self.cache[key] = [value, 1]
            self.space -= 1
            

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)