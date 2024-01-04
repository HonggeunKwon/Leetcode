class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Map<Character, Integer> map = new HashMap<>();
        
        int stoenLength = stones.length();
        
        for (int i = 0; i < stoenLength; i++) {
            char c = stones.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        int answer = 0;
        
        for (char c : jewels.toCharArray()) {
            answer += map.getOrDefault(c, 0);
        }
        
        return answer;
    }
}