class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        answer = 0
        
        jewel_set = set(jewels)
        
        for c in stones:
            if c in jewel_set:
                answer += 1
        
        return answer
                
        