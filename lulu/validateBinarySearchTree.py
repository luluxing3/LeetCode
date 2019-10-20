# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return (self.isValidBST(root.left) and self.isValidBST(root.right) and
                root.val > self.findMaximum(root.left) and
                root.val < self.findMinimum(root.right))
        else:
            return True
    
    def findMinimum(self, root):
        p = root
        while p and p.left:
            p = p.left
        if p:
            return p.val
        else:
            return float('inf')
    
    def findMaximum(self, root):
        p = root
        while p and p.right:
            p = p.right
        if p:
            return p.val
        else:
            return -float('inf')
