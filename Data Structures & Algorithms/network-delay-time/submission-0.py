class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dest, wt in times:
            adj[src].append((dest, wt))
        
        minheap = [(0, k)] # [weight, source]
        visited = set()
        t = 0 # result

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minheap, [w2 + w1, n2])
        
        return t if len(visited) == n else -1
        # time complexity: O(E * log V)