/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> rets = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();
        DFS(root, sum, rets, path);
        
        return rets;
    }
    
    public void DFS(TreeNode root, int sum, List<List<Integer>> rets, List<Integer> path) {
        if (root == null)
            return;
        
        path.add(root.val);
        sum -= root.val;
        if (root.left == null && root.right == null && sum == 0)
            rets.add(new ArrayList<>(path));
        
        DFS(root.left, sum, rets, path);
        DFS(root.right, sum, rets, path);
        sum += root.val;
        path.remove(path.size() - 1);
    }
}