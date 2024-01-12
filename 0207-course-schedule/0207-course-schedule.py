class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = collections.defaultdict(list)
        
        for course, pre in prerequisites:
            course_dict[pre].append(course)
        
        visited = {}
        
        def cycle(node, tracker, visited) -> bool:
            tracker[node] = True
            visited[node] = True
            for next_course in course_dict[node]:
                if next_course not in visited and cycle(next_course, tracker, visited):
                    return True
                elif next_course in tracker:
                    return True
            tracker.pop(node)
            return False
        
        for course in range(numCourses):
            if course not in visited and cycle(course, {}, visited):
                return False
        
        return True
    