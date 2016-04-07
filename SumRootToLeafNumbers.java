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
    public int sumNumbers(TreeNode root) {
        return DFS(root, 0);
    }
    
    public int DFS(TreeNode root, int num) {
        if (root == null)
            return 0;
        
        num = num * 10 + root.val;
        if (root.left == null && root.right == null)
            return num;
        
        return DFS(root.left, num) + DFS(root.right, num);
    }
}