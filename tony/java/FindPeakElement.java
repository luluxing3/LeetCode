public class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1)
            return 0;
        
        int low = 0;
        int high = nums.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (mid == 0)
                return nums[mid] > nums[mid + 1] ? mid : mid + 1;
            if (mid == nums.length - 1 && nums[mid] > nums[mid - 1])
                return mid;
            
            if (nums[mid - 1] < nums[mid] && nums[mid] > nums[mid + 1]) {
                return mid;
            } else if (nums[mid - 1] <= nums[mid + 1]) {
                low = mid + 1;
            } else if (nums[mid - 1] > nums[mid + 1]) {
                high = mid - 1;
            }
        }
        
        return -1;
    }
}