/**
 * 此方法不能解决返回list中的triplet三元组顺序的问题
 */
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        quickSort(nums, 0, nums.length - 1);
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            int target = 0 - nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                int diff = target - nums[j];
                if (map.containsKey(diff)) {
                    list.add(nums[i]);
                    list.add(diff);
                    list.add(nums[j]);
                    res.add(list);
                    list = new ArrayList<Integer>();
                }
                map.put(nums[j], j);
            }
            map.clear();
        }
        
        return res;
    }
    
    public void quickSort(int[] nums, int low, int high) {
        if (low < high) {
            int mid = partition(nums, low, high);
            quickSort(nums, low, mid - 1);
            quickSort(nums, mid + 1, high);
        }
    }
    
    public int partition(int[] nums, int low, int high) {
        int pivot = nums[low];
        
        while (low < high) {
            while (low < high && nums[high] >= pivot)
                high--;
            nums[low] = nums[high];
            while (low < high && nums[low] <= pivot)
                low++;
            nums[high] = nums[low];
        }
        nums[low] = pivot;
        
        return low;
    }
}