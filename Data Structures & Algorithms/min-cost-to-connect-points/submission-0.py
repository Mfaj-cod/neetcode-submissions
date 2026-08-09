class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = { i:[] for i in range(len(points)) }
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j]) # src: [wt, dest]
                adj[j].append([dist, i])

        # Prim's
        minheap = [(0, 0)] # (dist, dest)
        visited = set()
        total = 0 # min cost
        while len(visited) < len(points):
            dist, point = heapq.heappop(minheap)
            if point in visited:
                continue
                
            visited.add(point)
            total += dist

            for d, p in adj[point]:
                if p not in visited:
                    heapq.heappush(minheap, (d, p))
        
        return total