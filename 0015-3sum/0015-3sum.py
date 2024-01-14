class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_length = len(nums)
        answer = []
        for i in range(nums_length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            lt, rt = i + 1, nums_length - 1
            
            while lt < rt:
                total = nums[i] + nums[lt] + nums[rt]
                
                if total > 0:
                    rt -= 1
                elif total < 0:
                    lt += 1
                else:
                    answer.append([nums[i], nums[lt], nums[rt]])
                    
                    while lt < rt and nums[lt] == nums[lt + 1]:
                        lt += 1
                    while lt < rt and nums[rt] == nums[rt - 1]:
                        rt -= 1
                    lt += 1
                    rt -= 1
        return answer