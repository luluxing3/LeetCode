# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        #print('inorder: %s' %inorder)
        #print('post: %s' %postorder)
        root_val = postorder[-1]
        divide_index = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[: divide_index], postorder[: divide_index])
        root.right = self.buildTree(inorder[divide_index + 1: ], postorder[divide_index : -1])
        return root
