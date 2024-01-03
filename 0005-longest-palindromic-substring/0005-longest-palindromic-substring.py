class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isAnagram(s:str, left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        str_len = len(s)
            
        for length in range(str_len, 0, -1):
            for start_idx in range(0, str_len - length + 1):
                if isAnagram(s, start_idx, start_idx + length - 1):
                    return s[start_idx:(start_idx + length)]                
                
        return ''