import java.util.*;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        Stack<Integer> s = new Stack<>();
        
        for (int i = 0; i < temperatures.length; i++) {
            while (!s.isEmpty() && temperatures[s.peek()] < temperatures[i]) {                
                int preIdx = s.pop();
                answer[preIdx] = i - preIdx;
            }
            s.push(i);
        }
        
        return answer;
        
    }
}