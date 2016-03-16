
public class Solution {
    public int countPrimes(int n) {
    	// 0代表是素数，1代表不是素数
        int[] nums = new int[n];
        for (int i = 2; i * i < n; i++) {
            if (nums[i] == 0) {
                for (int j = i; i * j < n; j++) {
                    nums[i * j] = 1;
                }
            }
        }
        
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (nums[i] == 0)
                count++;
        }
        return count;
    }
}