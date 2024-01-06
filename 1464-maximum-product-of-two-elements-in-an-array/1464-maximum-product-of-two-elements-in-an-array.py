class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for lt in range(len(nums)):
            max_value = nums[lt]
            idx = lt
            for rt in range(lt + 1, len(nums)):
                if max_value < nums[rt]:
                    max_value = nums[rt]
                    idx = rt
            nums[lt], nums[idx] = nums[idx], nums[lt]
        
        return (nums[0] - 1) * (nums[1] - 1)
            