public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums.length == 0)
            return 0;
        
        int min = nums.length + 1;
        int i = 0, j = 0, sum = nums[0];
        while (j < nums.length) {
            if (sum >= s) {
                min = min > (j-i+1) ? (j-i+1) : min;
                if (min == 1)
                    return min;
                sum -= nums[i++];
            } else {
                j++;
                if (j < nums.length)
                    sum += nums[j];
            }
        }

        return min == nums.length - 1 ? 0 : min;
    }

    public int minSubArrayLen_2(int s, int[] nums) {
        if (nums.length == 0)
            return 0;
        
        int min = nums.length + 1;
        int i = 0, j = 0, sum = 0;
        while (j < nums.length) {
            sum += nums[j];
            while (sum >= s) {
                min = min > (j-i+1) ? (j-i+1) : min;
                if (min == 1)
                    break;
                sum -= nums[i++];
            }
            j++;
        }

        return min == nums.length + 1 ? 0 : min;
    }
}