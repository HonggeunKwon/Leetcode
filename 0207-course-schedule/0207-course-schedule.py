class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ticket_dict = collections.defaultdict(list)
        
        for course, pre in prerequisites:
            ticket_dict[pre].append(course)
        
        visited = {}
        def has_cycle(node, tracker, visited) -> bool:
            tracker[node] = True
            visited[node] = True
            
            for next_course in ticket_dict[node]:
                if next_course not in visited and has_cycle(next_course, tracker, visited):
                    return True
                elif next_course in tracker:
                    return True
            tracker.pop(node)
            return False
            
        
        for i in range(numCourses):
            tracker = {}
            if i not in visited and has_cycle(i, tracker, visited):
                return False
        return True
