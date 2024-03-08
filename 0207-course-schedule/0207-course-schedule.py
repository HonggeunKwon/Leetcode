class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(list)
        
        for next_course, pre_course in prerequisites:
            courses[pre_course].append(next_course)
            
        visited = {}
        
        def is_cycle(node: int, tracker, visited) -> bool:
            tracker[node] = True
            visited[node] = True
            
            for next_course in courses[node]:
                if next_course not in visited and is_cycle(next_course, tracker, visited):
                    return True
                elif next_course in tracker:
                    return True
            tracker.pop(node)
            return False
        
        for i in range(numCourses):
            if i not in visited and is_cycle(i, {}, visited):
                return False
        
        return True