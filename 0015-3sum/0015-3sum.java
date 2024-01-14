class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            if (i != 0 && nums[i] == nums[i - 1]) continue;
            int lt = i + 1, rt = nums.length - 1;
            
            while(lt < rt) {
                int sum = nums[i] + nums[lt] + nums[rt];
                
                if (sum == 0){
                    answer.add(List.of(nums[i], nums[lt], nums[rt]));
                    
                    while (lt < rt && nums[lt] == nums[lt + 1]) {
                        lt++;
                    }
                    
                    while (lt < rt && nums[rt] == nums[rt - 1]) {
                        rt--;
                    }
                    
                    rt--;
                    lt++;                        
                }
                else if (sum > 0) {
                    rt--;
                } else {
                    lt++;
                }
            }
        }
        
        return answer;
        
    }
}