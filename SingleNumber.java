public class Solution {
    public int singleNumber(int[] nums) {
        // use xor to solve the problem
        for (int i = 1; i < nums.length; i++)
            nums[i] ^= nums[i - 1];
        return nums[nums.length - 1];
    }
}