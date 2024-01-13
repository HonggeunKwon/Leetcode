import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answer = new ArrayList<>();
        
        Map<String, List<String> > wordMap = new HashMap<>();
        for (String str: strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedWord = String.valueOf(chars);
            if (!wordMap.containsKey(sortedWord)) {
                wordMap.put(sortedWord, new ArrayList<>());
            }
            
            wordMap.get(sortedWord).add(str);
        }
        
        for (String key : wordMap.keySet()) {
            answer.add(wordMap.get(key));
        }
        
        return answer;
    }
}