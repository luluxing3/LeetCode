class Solution(object):
    def __init__(self):
        self.prev = None
        self.n1 = None
        self.n2 = None

    def findTwoNodes(self, root):
        if root:
            self.findTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                #maybe prev and root change directly
                #this is true only onece
                if self.n1 is None:
                    self.n1 = self.prev
                #else:      #wrong
                #    self.n2 = root  #wrong
                self.n2 = root
            self.prev = root
            self.findTwoNodes(root.right)
    def recoverTree(self, root):
        self.findTwoNodes(root)
        if self.n1 and self.n2:
            self.n1.val, self.n2.val = self.n2.val, self.n1.val
            

class Solution(object):
    def __init__(self):
        self.nodes = []

    def recoverTree(self, root):
        self.inorderTraversal(root)
        left_index = 0
        while left_index < len(self.nodes) - 1:
            if self.nodes[left_index].val <= self.nodes[left_index + 1].val:
                left_index += 1
            else:
                break
        right_index = len(self.nodes) - 1:
        while right_index > 0:
            if self.nodes[right_index].val >= self.nodes[right_index - 1].val:
                right_index -= 1
            else:
                break
        #swap
        self.nodes[left_index].val, self.nodes[right_index].val = self.nodes[right_index].val, self.nodes[left_index].val

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            self.nodes.append(root)
            self.inorderTraversal(root.right)

            
