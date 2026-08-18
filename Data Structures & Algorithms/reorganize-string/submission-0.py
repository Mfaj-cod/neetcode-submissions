class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = Counter(s)
        
        maxheap = [[-f, c] for c, f in hashmap.items()]
        heapq.heapify(maxheap)
        res = ""
        prev = None
        while maxheap or prev:
            if prev and not maxheap:
                return ""

            f, c = heapq.heappop(maxheap)
            # appending to res
            res += c
            # decrementing freq, since it's -ve, so add to decrement
            f += 1
            # push them again
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None

            if f != 0:
                prev = [f, c]
        
        return res