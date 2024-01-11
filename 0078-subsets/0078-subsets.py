class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        nums_len = len(nums)
        answer = []
        
        def dfs(L: int, picked: List[int]) -> None:
            if L == nums_len:
                subset = []
                for idx, value in enumerate(picked):
                    if value == 1:
                        subset.append(nums[idx])
                
                answer.append(subset)
                
                return
            
            picked[L] = 1
            dfs(L + 1, picked)
            picked[L] = 0
            dfs(L + 1, picked)
        
        dfs(0, [0] * nums_len)
        return answer
        
        