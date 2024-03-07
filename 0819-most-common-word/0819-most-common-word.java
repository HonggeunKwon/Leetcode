class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        
        paragraph = paragraph.toLowerCase().replaceAll("[^a-z ]", " ");
        Map<String, Integer> wordCounter = new HashMap<>();
        Set<String> banSet = new HashSet<>();
        String[] splits = paragraph.split(" ");
        for(String ban : banned) {
            banSet.add(ban);
        }
        
        for(int i = 0; i < splits.length; i++) {
            String word = splits[i];
            if(!banSet.contains(word) && !word.equals("")) {
                wordCounter.put(word, wordCounter.getOrDefault(word, 0) + 1);
            }
        }
        
        String answer = null;
        int max = 0;
        for (String key : wordCounter.keySet()) {
            if (max < wordCounter.get(key)) {
                max = wordCounter.get(key);
                answer = key;
            }
        }
        
        return answer;
    }
}