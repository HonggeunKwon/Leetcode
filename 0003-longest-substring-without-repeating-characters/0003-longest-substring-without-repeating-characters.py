class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = collections.defaultdict(int)
        
        lt = 0
        answer = 0
        
        for rt in range(len(s)):
            memo[s[rt]] += 1
            
            while memo[s[rt]] > 1:
                memo[s[lt]] -= 1
                lt += 1
            
            answer = max(answer, rt - lt + 1)
        
        return answer