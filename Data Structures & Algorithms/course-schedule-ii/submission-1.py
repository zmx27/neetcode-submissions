class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        res = []
        # Build indegree list and adj list
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs) # Prereq points to crs
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # Topological sort
        finish = 0
        while q:
            top = q.popleft() # Indegree 0 so no pre req
            res.append(top)
            finish += 1
            for pre in adj[top]: # Go through neighbors and decrement indegree
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
        
        return res if finish == numCourses else []
