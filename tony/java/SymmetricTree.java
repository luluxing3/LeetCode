public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        return isSymmetric(root.left, root.right);
    }
    
    // 构造一个重载方法
    public boolean isSymmetric(TreeNode lTree, TreeNode rTree) {
        if (lTree == null && rTree == null) {
            return true;
        } else if (lTree == null || rTree == null) {
            return false;
        }
        
        if (lTree.val != rTree.val) {
            return false;
        }
        return isSymmetric(lTree.left, rTree.right) && 
            isSymmetric(lTree.right, rTree.left);
    }
}