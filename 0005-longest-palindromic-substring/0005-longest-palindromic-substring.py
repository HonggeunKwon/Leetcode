class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int):
            str_len = len(s)
            while left >= 0 and right < str_len and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        str_len = len(s)
        
        if str_len < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(str_len - 1):
            result = max(result,
                expand(i, i + 1),
                expand(i, i + 2),
                        key=len)
        
        return result