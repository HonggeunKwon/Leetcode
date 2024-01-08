class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def dfs(S: int, L: int, picked: list[int]):
            if L == k:
                answer.append(copy.deepcopy(picked))
                return
            
            for i in range(S + 1, n + 1, 1):
                picked.append(i)
                dfs(i, L + 1, picked)
                picked.pop()
        
        
        dfs(0, 0, [])
        
        return answer