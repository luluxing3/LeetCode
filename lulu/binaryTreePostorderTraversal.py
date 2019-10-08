# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.postorderHelper(root)
        return self.ans
    
    def postorderHelper(self, root):
        if root:      
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            self.ans.append(root.val)
