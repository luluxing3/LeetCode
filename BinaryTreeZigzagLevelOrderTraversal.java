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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> lists = new ArrayList<List<Integer>>();
        List<Integer> list = null;
        int direct = 0; // odd is left, even is right
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
            if (direct++ % 2 == 1)
                Collections.reverse(list);
            lists.add(list);
        }
        
        return lists;
    }
}