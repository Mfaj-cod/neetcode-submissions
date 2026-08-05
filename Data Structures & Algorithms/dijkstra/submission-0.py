class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        
        for s, dst, wet in edges:
            adj_list[s].append([dst, wet])
        
        shortest = {} # map vertex to dist of the shortest path
        minheap = [[0, src]]

        while minheap:
            weight1, node = heapq.heappop(minheap)
            if node in shortest:
                continue
            
            shortest[node] = weight1

            for neighbour, weight2 in adj_list[node]:
                if neighbour not in shortest:
                    heapq.heappush(minheap, [weight2 + weight1, neighbour])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
