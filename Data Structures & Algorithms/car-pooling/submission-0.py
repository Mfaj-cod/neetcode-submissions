class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minheap = [] # pair of [end, numofpassengers]
        currPas = 0

        for psngr, frm, too in trips:

            while minheap and minheap[0][0] <= frm:
                currPas -= minheap[0][1]
                heapq.heappop(minheap)

            currPas += psngr
            if currPas > capacity:
                return False
            heapq.heappush(minheap, (too, psngr))

        return True