public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0)
            return 0;
        
        int len = 1;
        int[] d = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            d[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i] && d[j] + 1 > d[i])
                    d[i] = d[j] + 1;
                if (d[i] > len)
                    len = d[i];
            }
        }
        
        return len;
    }
}