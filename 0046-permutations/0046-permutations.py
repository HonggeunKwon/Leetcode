class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        answer = []
        used = [False] * nums_len
        
        def dfs(L, arr):
            if L == nums_len:
                answer.append(copy.deepcopy(arr))
                return
            
            for i in range(nums_len):
                if not used[i]:
                    used[i] = True
                    arr.append(nums[i])                    
                    dfs(L + 1, arr)
                    arr.pop()
                    used[i] = False
                    
        
        if nums:
            dfs(0, [])
        
        return answer