# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return q.val == p.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        else:
            return (p is None) and (q is None)
