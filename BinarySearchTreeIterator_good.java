/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator {
    List<Integer> vals = new ArrayList<Integer>();
    int pointer;
    int size;

    public void inOrder(TreeNode root) {
        if (root != null) {
            inOrder(root.left);
            vals.add(root.val);
            inOrder(root.right);
        }
    }

    public BSTIterator(TreeNode root) {
        inOrder(root);
        pointer = 0;
        size = vals.size();
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return pointer < size;
    }

    /** @return the next smallest number */
    public int next() {
        return vals.get(pointer++);
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */