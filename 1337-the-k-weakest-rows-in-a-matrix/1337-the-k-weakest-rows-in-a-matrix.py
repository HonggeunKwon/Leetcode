class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            value = mat[i].count(1)
            heapq.heappush(heap, (value, i))
        
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])      
        
        return answer
            