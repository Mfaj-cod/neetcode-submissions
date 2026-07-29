class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = { i:[] for i in range(numCourses) }
        # mapping all the prerequisites to the course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # set for saving visited nodes
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []

        return res