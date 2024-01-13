class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = collections.defaultdict(list)
        
        for word in strs:
            word_dict[''.join(sorted(word))].append(word)
        
        return list(word_dict.values())