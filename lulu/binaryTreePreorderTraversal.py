# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.preorderHelper(root)
        return self.ans
    
    def preorderHelper(self, root):
        if root:
            self.ans.append(root.val)
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)
