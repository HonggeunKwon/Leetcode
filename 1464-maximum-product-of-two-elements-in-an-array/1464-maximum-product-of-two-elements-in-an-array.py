class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        
        return (heapq.heappop(nums) + 1) * (heapq.heappop(nums) + 1)
        