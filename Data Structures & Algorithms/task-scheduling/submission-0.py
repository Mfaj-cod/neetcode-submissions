class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task n unit time
        # minimize idle time
        # TC O(n(len of tasks) * m(size of given n))
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-c, idleTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # adding 1 because it has negative values, so it will decrease it
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time