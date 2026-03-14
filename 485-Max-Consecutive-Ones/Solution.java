class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int consecutive = 0;
        int consecutiveTrial = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                consecutiveTrial++;
            }else{
                consecutive = Math.max(consecutive, consecutiveTrial);
                consecutiveTrial = 0;
            }
        }
        consecutive = Math.max(consecutive, consecutiveTrial);

        return consecutive;
    }
}