class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxheap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxheap, (count, char))

        while maxheap:
            freq, char = heapq.heappop(maxheap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxheap:
                    break
                freq2, char2 = heapq.heappop(maxheap)
                res += char2
                freq2 += 1

                if freq2:
                    heapq.heappush(maxheap, (freq2, char2))
            else:
                res += char
                freq += 1

            if freq:
                heapq.heappush(maxheap, (freq, char))

        return res
