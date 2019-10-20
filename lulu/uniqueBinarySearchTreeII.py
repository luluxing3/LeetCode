# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        else:
            return self.helper(1, n + 1)
    
    def helper(self, start, end):
        if start >= end:
            return [None]
        else:
            ans = []
            for i in range(start, end):
                leftSubtrees = self.helper(start, i)
                rightSubtrees = self.helper(i + 1, end)
                for left in leftSubtrees:
                    for right in rightSubtrees:
                        p = TreeNode(i)
                        p.left = left
                        p.right = right
                        ans.append(p)
            return ans
