class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = collections.deque() 
        
        for c in s:
            if c.isalnum():
                d.append(c.lower())
        
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True