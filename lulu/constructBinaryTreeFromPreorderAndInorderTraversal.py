# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root_val = preorder[0]
        root_index = inorder.index(root_val)
        left_inorder = inorder[: root_index]
        right_inorder = inorder[root_index + 1:]
        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]
        
        root = TreeNode(root_val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
        
        
        
        
