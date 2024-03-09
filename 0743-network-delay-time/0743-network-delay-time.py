class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for start, end, cost in times:
            graph[start].append((end, cost))
        
        q = [(0, k)]
        dist = collections.defaultdict(int)
        
        while q:
            cost, node = heapq.heappop(q)
            
            if node not in dist:
                dist[node] = cost
                
                for next_node, next_cost in graph[node]:
                    heapq.heappush(q, (next_cost + cost, next_node))
        
        if len(dist) == n:
            return max(dist.values())
        return -1
            