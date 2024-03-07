class Solution {
    public String longestPalindrome(String s) {
        String answer = null;
        int maxLen = 0;
        
        if(s.length() < 2) {
            return s;
        }
        
        for (int i = 0; i < s.length() - 1; i++) {
            String a = this.getPalindrome(s, i, i + 1);
            String b = this.getPalindrome(s, i, i + 2);
            
            if(a.length() > maxLen) {
                answer = a;
                maxLen = a.length();
            }
            
            if(b.length() > maxLen) {
                answer = b;
                maxLen = b.length();
            }
        }
        
        return answer;
    }
    
    public String getPalindrome(String s, int lt, int rt) {
        int strLen = s.length();
        while (lt >= 0 && rt < strLen && s.charAt(lt) == s.charAt(rt)) {
            lt--;
            rt++;
        }
        
        return s.substring(lt + 1, rt);
    }
}