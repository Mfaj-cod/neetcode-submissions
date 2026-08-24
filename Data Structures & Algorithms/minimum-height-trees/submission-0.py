class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        edge_count = {}
        leaves = deque()
        for src, neighbours in adj.items():
            if len(neighbours) == 1:
                leaves.append(src)
            edge_count[src] = len(neighbours)
        
        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)
