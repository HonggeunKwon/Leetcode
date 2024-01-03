
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for(int i = 0; i < strs.length; i++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);
            if(!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            
            map.get(key).add(strs[i]);
        }
        
        List<List<String> > answer = new ArrayList<>();
        for (String key : map.keySet()) {
            answer.add(map.get(key));
        }
        
        return answer;
    }
}