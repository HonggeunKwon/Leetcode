class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> digits = new ArrayList<>();
        List<String> letters = new ArrayList<>();
        
        for (String log : logs) {
            if(Character.isDigit(log.split(" ")[1].charAt(0))) {
                digits.add(log);
            } else {
                letters.add(log);
            }
        }
        
        letters.sort((o1, o2) -> {
                String identifier1 = o1.split(" ")[0];
                String logWoIdentifier1 = o1.substring(identifier1.length());

                String identifier2 = o2.split(" ")[0];
                String logWoIdentifier2 = o2.substring(identifier2.length());

                if (logWoIdentifier1.compareTo(logWoIdentifier2) == 0) {
                    return identifier1.compareTo(identifier2);
                }

                return logWoIdentifier1.compareTo(logWoIdentifier2);                
        });
        
        letters.addAll(digits);
        
        return letters.toArray(new String[0]);
    }
}