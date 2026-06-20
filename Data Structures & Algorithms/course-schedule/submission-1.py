class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            cMap[course].append(prereq)
        
        visited = set() # Store all courses along the curr dfs path
        def dfs(course):
            if (course in visited):
                return False
            
            if cMap[course] == []:
                return True
            
            visited.add(course)
            for pre in cMap[course]:
                if (not dfs(pre)):
                    return False
            visited.remove(course)
            cMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
