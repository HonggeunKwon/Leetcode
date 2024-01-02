class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        counts = 0
        for char in jewels:
            counts += freqs[char]
        return counts