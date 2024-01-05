class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_map = collections.defaultdict(int)
        
        lt, rt = 0, 0
        s_len = len(s)
        answer = 0
        
        while lt <= rt and rt < s_len:
            substring_map[s[rt]] += 1
            while substring_map[s[rt]] > 1:
                substring_map[s[lt]] -= 1
                lt += 1
            answer = max(answer, rt - lt + 1)
            rt += 1
        
        return answer