class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.space = capacity

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        
        if len(self.cache) >= self.space:
            # popitem(last=False) removes and returns the (LRU) item in O(1)
            self.cache.popitem(last=False)
        # inserting new
        self.cache[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)