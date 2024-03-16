class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = {}
        
        def is_cycle(node, visited, tracker):            
            visited[node] = True
            tracker[node] = True
            
            for next_node in graph[node]:
                if next_node not in visited and is_cycle(next_node, visited, tracker):
                    return True
                elif next_node in tracker:
                    return True
            tracker.pop(node)            
            return False
            
        
        for i in range(numCourses):
            if i not in visited and is_cycle(i, visited, {}):
                return False
        
        return True