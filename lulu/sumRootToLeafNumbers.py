# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.nums = []
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traversal(root, 0)
        return sum(self.nums)
    def traversal(self, root, cur):
        if root is None:
            return
        if root and root.left is None and root.right is None:
            #leaf
            oneNum = 10 * cur + root.val
            self.nums.append(oneNum)
        if root:
            cur = 10 * cur + root.val
            self.traversal(root.left, cur)
            self.traversal(root.right, cur)
