class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = dict()
        graph = collections.defaultdict(list)
        
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
            
        
        min_heap = [(0, src, 0)]
        
        while min_heap:
            cost, current, stopover = heapq.heappop(min_heap)
            if current == dst:
                return cost
            if current not in visited or visited[current] > stopover:
                visited[current] = stopover
                if stopover <= k:
                    for next_node, next_cost in graph[current]:
                        heapq.heappush(min_heap, (next_cost + cost, next_node, stopover + 1))
        return -1