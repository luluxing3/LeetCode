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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> lists = new ArrayList<List<Integer>>();
        visit(root, lists, 0);
        
        return lists;
    }
    
    public void visit(TreeNode cur, List<List<Integer>> lists, int level) {
        if (cur == null)
            return;
        
        if (lists.size() < level + 1)
            lists.add(new ArrayList<Integer>());
        lists.get(level).add(cur.val);
        
        visit(cur.left, lists, level + 1);
        visit(cur.right, lists, level + 1);
    }
}