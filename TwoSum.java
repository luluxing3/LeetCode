public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            Integer diff = target - nums[i];
            if (map.containsKey(diff)) {
                int[] indices = {map.get(diff), i};
                return indices;
            }

            map.put(nums[i], i);
        }

        return null;
    }
}