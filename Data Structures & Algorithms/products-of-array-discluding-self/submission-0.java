class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        if (nums == null || nums.length == 0) {
            return result;
        }

        int[] prefixSum = new int[nums.length];
        int[] suffixSum = new int[nums.length];
        prefixSum[0] = 1;
        int prefix = 1;
        for (int i = 1; i < nums.length; i++) {
            prefix = prefix * nums[i - 1];
            prefixSum[i] = prefix;
        }
        suffixSum[nums.length - 1] = 1;
        int suffix = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            suffix = suffix * nums[i + 1];
            suffixSum[i] = suffix;
        }

        for (int i = 0; i < nums.length; i++) {
            result[i] = prefixSum[i] * suffixSum[i];
        }

        return result;
    }
}  
