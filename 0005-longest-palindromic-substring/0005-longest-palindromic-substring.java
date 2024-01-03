class Solution {
    public String longestPalindrome(String s) {
        int s_len = s.length();
        
        String result = "";
        
        if (s_len < 2) return s;
        
        for (int i = 0; i < s_len - 1; i++) {
            String even = expand(s, i, i + 1);
            String odd = expand(s, i, i + 2);
            
            if (result.length() < even.length()) {
                result = even;
            }
            if (result.length() < odd.length()) {
                result = odd;
            }
        }
        
        return result;
    }
    
    private static String expand(String s, int left, int right) {
        int sLen = s.length();
        while(left >= 0 && right < sLen && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        
        return s.substring(left + 1, right);
    }
}