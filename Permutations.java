public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        DFS(nums, 0, ret);
        
        return ret;
    }
    
    public void DFS(int[] nums, int start, List<List<Integer>> ret) {
        if (start == nums.length - 1) {
            Integer[] arr = new Integer[nums.length];
            for (int i = 0; i < nums.length; i++)
                arr[i] = nums[i];
            List<Integer> list = Arrays.asList(arr);
            ret.add(list);
        } else {
            for (int i = start; i < nums.length; i++) {
                swap(nums, start, i);
                DFS(nums, start + 1, ret);
                swap(nums, start, i); // backtracking
            }
        }
    }
    
    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    public boolean isSwap(int[] nums, int start, int end) {
        for (; start < end; start++)
            if (nums[start] == nums[end])
                return false;
        return true;
    }
}