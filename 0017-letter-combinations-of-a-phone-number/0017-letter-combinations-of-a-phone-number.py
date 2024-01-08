class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        input_len = len(digits)
        answer = []
        digit_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def dfs(L, currStr):
            if len(currStr) == input_len:
                answer.append(currStr)
                return
            
            for c in digit_dict[digits[L]]:
                dfs(L + 1, currStr + c)
        
        if digits:
            dfs(0, '')
        
        return answer