class Solution {
    private int wordLength;
    
    public String longestPalindrome(String s) {
        int maxLength = 0;
        String answer = null;
        this.wordLength = s.length();
        if (wordLength == 1) {
            return s;
        }
        
        for(int i = 0; i < wordLength - 1; i++) {
            String even = getLongestPalindrom(s, i, i + 1);
            String odd = getLongestPalindrom(s, i, i + 2);
            
            if (maxLength < even.length()) {
                maxLength = even.length();
                answer = even;
            }
            
            if (maxLength < odd.length()) {
                maxLength = odd.length();
                answer = odd;
            }
        }
        
        return answer;
    }
    
    private String getLongestPalindrom(String word, int left, int right) {
        
        while (left >= 0 && right < word.length() && word.charAt(left) == word.charAt(right)) {
            left--;
            right++;
        }
        
        return word.substring(left + 1, right);
    }
}