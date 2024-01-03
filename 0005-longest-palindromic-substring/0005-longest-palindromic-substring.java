class Solution {
    static int len = 0;
    public String longestPalindrome(String s) {
        String answer = "";
        len = s.length();
        
        if (s.length() < 2) return s;
        
        for (int i = 0; i < len - 1; i++) {
            String first = expand(i, i + 1, s);
            String second = expand(i, i + 2, s);
            
            if (answer.length() < first.length()) {
                answer = first;
            }
            if (answer.length() < second.length()) {
                answer = second;
            }
        }
            
        return answer;
    }
    
    static String expand(int left, int right, String s) {
        while (left >= 0 && right < len && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        
        return s.substring(left + 1, right);
    }
}