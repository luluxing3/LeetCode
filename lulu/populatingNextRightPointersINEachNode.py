class Solution(object):
    def __init__(self):
        self.nodes = []
    def traversal(self, root, level):
        if root:
            if level == len(self.nodes):
                self.nodes.append([])
            self.nodes[level].append(root)
            self.traversal(root.left, level + 1)
            self.traversal(root.right, level + 1)

    def connect(self, root):
        self.traversal(root, 0)
        for level_nodes in self.nodes:
            for index in range(len(level_nodes) - 1):
                level_nodes[index].next = level_nodes[index + 1]
        return root

                

