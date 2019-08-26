public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        DFS(candidates, target, 0, 0, list, ret);
        return ret;
    }
    
    public void DFS(int[] candidates, int target, int sum, int k, List<Integer> list, List<List<Integer>> ret) {
		if (sum > target) {
			return;
		} else if (sum == target) {
			ret.add(new ArrayList<Integer>(list));
			return;
		} else {
			for (int i = k; i < candidates.length; i++) {
			    if (i != k && candidates[i] == candidates[i - 1])
			        continue;
				sum += candidates[i];
				list.add(candidates[i]);
				DFS(candidates, target, sum, i + 1, list, ret);
				list.remove(list.size() - 1);
				sum -= candidates[i];
			}
		}
	}
}