class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(list)
        
        def is_cycle(node, visited, tracker):
            visited[node] = True
            tracker[node] = True
            
            for i in courses[node]:
                if i not in visited and is_cycle(i, visited, tracker):
                    return True
                elif i in tracker:
                    return True
            tracker.pop(node)
            return False
        
        
        for after, before in prerequisites:
            courses[before].append(after)
        
        visited = {}
        
        for i in range(numCourses):
            if i not in visited and is_cycle(i, visited, {}):
                return False
        
        return True