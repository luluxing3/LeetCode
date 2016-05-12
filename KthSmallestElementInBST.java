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
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> s = new Stack<TreeNode>();
        TreeNode cur = root;
        
        while (!s.isEmpty() || cur != null) {
            while (cur != null) {
                s.push(cur);
                cur = cur.left;
            }
            if (!s.isEmpty()) {
                cur = s.pop();
                if (--k == 0)
                    break;
                cur = cur.right;
            }
        }
        return cur.val;
    }
    
    public void inOrder(TreeNode root, int k, int[] rets) {
        if (root == null || rets[0] == k)
            return;
        
        inOrder(root.left, k, rets);
        if (++rets[0] == k)
            rets[1] = root.val;
        inOrder(root.right, k, rets);
    }
}