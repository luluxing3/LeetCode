# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.helper(root, 0)
        ans = []
        for i in range(len(self.ans) - 1, -1, -1):
            ans.append(self.ans[i])
        return ans
    
    def helper(self, root, level):
        if root:
            if level >= len(self.ans):
                self.ans.append([])
                
            self.ans[level].append(root.val)
            self.helper(root.left, level + 1)
            self.helper(root.right, level + 1)
