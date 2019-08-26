public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int closestTarget = 0;
        int min = Integer.MAX_VALUE;
        
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            int low = i + 1;
            int high = nums.length - 1;
            while (low < high) {
                int sum = nums[i] + nums[low] + nums[high];
                if (sum == target) {
                    return sum;
                } else if (sum < target) {
                    if (target - sum < min) {
                        min = target - sum;
                        closestTarget = sum;
                    }
                    low++;
                } else {
                    if (sum - target < min) {
                        min = sum - target;
                        closestTarget = sum;
                    }
                    high--;
                }
            }
        }
        
        return closestTarget;
    }
}