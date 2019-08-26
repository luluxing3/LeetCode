public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums.length == 0)
            return 0;
        
        int min = nums.length + 1;
        int[] sums = new int[nums.length + 1];
        for (int i = 1; i < sums.length; i++)
            sums[i] = sums[i - 1] + nums[i - 1];
            
        for (int i = 1; i < sums.length; i++) {
            int high = binarySearch(i, sums.length - 1, sums[i - 1] + s, sums);
            if (high == sums.length)
                break;
            min = min > (high-i+1) ? (high-i+1) : min;
        }
        
        return min == nums.length + 1 ? 0: min;
    }
    
    public int binarySearch(int low, int high, int key, int[] sums) {
        while (low <= high) {
            int mid = (low + high) / 2;
            if (sums[mid] >= key) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return low;
    }
}