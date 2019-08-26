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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> lists = new ArrayList<List<Integer>>();
        List<Integer> list = null;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        if (root != null)
            queue.offer(root);
        
        while (!queue.isEmpty()) {
            list = new ArrayList<Integer>();
            int size = queue.size();
            
            while (size-- > 0) {
                TreeNode cur = queue.poll();
                list.add(cur.val);
                
                if (cur.left != null)
                    queue.offer(cur.left);
                if (cur.right != null)
                    queue.offer(cur.right);
            }
            lists.add(list);
        }
        
        Collections.reverse(lists);
        return lists;
    }
}
