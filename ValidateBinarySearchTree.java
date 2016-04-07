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
    TreeNode pre = null;
    
    public boolean isValidBST(TreeNode root) {
        if (root == null)
            return true;
        
        
        if (!isValidBST(root.left))
            return false;
        if (pre != null && pre.val >= root.val)
            return false;
        pre = root;
        if (!isValidBST(root.right))
            return false;
        
        return true;
    }
}