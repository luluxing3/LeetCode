# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.pathSumHelper(root, sum, [])
        return self.ans
    def pathSumHelper(self, root, gap, cur):
        if root is None:
            return
        if root.left is None and root.right is None:
            if gap == root.val:
                cur.append(root.val)
                self.ans.append(cur)
                return
        
        cur.append(root.val)
        self.pathSumHelper(root.left, gap - root.val, cur[:])
        self.pathSumHelper(root.right, gap - root.val, cur[:])
