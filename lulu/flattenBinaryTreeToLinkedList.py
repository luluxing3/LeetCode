class Solution(object):
    def flatten(self, root):
        if root:
            left = root.left
            right = root.right
            root.left = None
            root.right = self.flatten(left)
            tail = root
            while tail and tail.right:
                tail = tail.right
            tail.right = self.flatten(right)
        return root
                
                
