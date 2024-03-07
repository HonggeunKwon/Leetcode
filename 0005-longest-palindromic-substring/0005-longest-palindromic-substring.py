class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(lt: int, rt: int) -> str:
            while lt >= 0 and rt < len(s) and s[lt] == s[rt]:
                lt -= 1
                rt += 1
            return s[lt + 1:rt]
        
        answer = ''
        
        if len(s) <= 1 or s == s[::-1]:
            return s
        
        for i in range(len(s) - 1):
            answer = max(answer, expand(i, i + 1), expand(i, i + 2), key=len)
            
        return answer