class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = collections.defaultdict(list)
        
        for word in strs:
            anagram_dict[''.join(sorted(word))].append(word)
        
        return list(anagram_dict.values())