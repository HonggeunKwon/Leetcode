class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        nums_len = len(nums)
        answer = []
        
        def dfs(L: int, picked: List[int]) -> None:
            if L == nums_len:
                subset = []
                for idx, value in enumerate(picked):
                    if value:
                        subset.append(nums[idx])
                
                answer.append(subset)                
                return
            
            picked[L] = True
            dfs(L + 1, picked)
            picked[L] = False
            dfs(L + 1, picked)
        
        dfs(0, [False] * nums_len)
        return answer
        
        