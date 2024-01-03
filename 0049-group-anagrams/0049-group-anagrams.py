class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = collections.defaultdict(list)
        
        for str in strs:
            key = sorted(str)
            anagram_dict[''.join(key)].append(str)
            
#       CASE #1
        answer = list(anagram_dict.values())
        answer.sort(key=len)

        return answer
        # return list(anagram_dict.values()).sort(key=len)