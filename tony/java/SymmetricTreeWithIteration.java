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
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }

        Queue<TreeNode> q1 = new LinkedList<TreeNode>();
        Queue<TreeNode> q2 = new LinkedList<TreeNode>();
        q1.offer(root.left);
        q2.offer(root.right);

        while (!q1.isEmpty()) {
            TreeNode lchild = q1.poll();
            TreeNode rchild = q2.poll();

            if (lchild == null && rchild == null) {
                continue;
            } else if (lchild == null || rchild == null) {
                return false;
            }

            if (lchild.val != rchild.val) {
                return false;
            }
            q1.offer(lchild.left);
            q1.offer(lchild.right);
            q2.offer(rchild.right);
            q2.offer(rchild.left);
        }

        return true;
    }
}

