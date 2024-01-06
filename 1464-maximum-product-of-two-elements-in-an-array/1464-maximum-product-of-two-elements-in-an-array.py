class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        return (lambda x: x[0]*x[1])([i-1 for i in heapq.nlargest(2, nums)])
        