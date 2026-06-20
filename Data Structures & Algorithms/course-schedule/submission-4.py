class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        # Build indegree list
        for course, prereq in prerequisites:
            indegree[course] += 1 # Indegree represents number of pre reqs
            adj[prereq].append(course) # Pre reqs point to the course
        
        # Add courses with no pre reqs for processing
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0: # No pre req
                q.append(n)
        
        # Process the courses
        finish = 0
        while q:
            top = q.popleft() # Courses with no pre reqs are processed
            finish += 1
            for nei in adj[top]:
                indegree[nei] -= 1 # If this is pre req of another course, delete it
                if indegree[nei] == 0:
                    q.append(nei) # Add more courses with no more pre reqs for processing
        return finish == numCourses
