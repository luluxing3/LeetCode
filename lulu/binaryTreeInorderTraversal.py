# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorderHelper(root)
        return self.ans
    
    def inorderHelper(self, root):
        if root:
            self.inorderHelper(root.left)
            self.ans.append(root.val)
            self.inorderHelper(root.right)
