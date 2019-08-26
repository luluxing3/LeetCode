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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> rets = new ArrayList<String>();
        String path = "";
        DFS(root, rets, path);
        
        return rets;
    }
    
    public void DFS(TreeNode root, List<String> rets, String path) {
        if (root == null)
            return;
        
        path += root.val + "->";
        if (root.left == null && root.right == null) {
            path = path.substring(0, path.length() - 2);
            rets.add(new String(path));
        }
        
        DFS(root.left, rets, path);
        DFS(root.right, rets, path);
        
        path += "->";
        path = path.substring(0, path.length() - 3);
    }
}