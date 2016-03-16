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
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        int leftDepth = treeDepth(root.left);
        int rightDepth = treeDepth(root.right);
        if (Math.abs(leftDepth - rightDepth) > 1) {
            return false;
        }
        
        return isBalanced(root.left) && isBalanced(root.right);
    }
    
    public int treeDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftDepth = treeDepth(root.left);
        int rightDepth = treeDepth(root.right);
        
        return leftDepth > rightDepth ? (leftDepth + 1) : (rightDepth + 1);
    }
}