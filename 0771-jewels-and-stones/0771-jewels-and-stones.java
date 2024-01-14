import java.util.*;

class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> jewelSet = new HashSet<>();
        
        for (char c: jewels.toCharArray()) {
            jewelSet.add(c);
        }
        int answer = 0;
        
        for (char s : stones.toCharArray()) {
            if (jewelSet.contains(s)) {
                answer += 1;
            }
        }
        
        return answer;
        
    }
}