# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.ans = []
    def levelOrder(self, root):
        current_queue = []
        next_queue = []
        if root:
            current_queue.append(root)
        else:
            return self.ans
        while current_queue:
            level_list = []
            while current_queue:
                p = current_queue.pop(0)
                level_list.append(p.val)
                if p.left:
                    next_queue.append(p.left)
                if p.right:
                    next_queue.append(p.right)
            self.ans.append(level_list)
            current_queue, next_queue = next_queue, current_queue
        return self.ans
            

class Solution(object):
    def __init__(self):
        self.ans = []
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.levelOrderHelper(root, 1)
        return self.ans
            
    def levelOrderHelper(self, root, level):
        if root is None:
            return
        else:
            if level <= len(self.ans):
                self.ans[level - 1].append(root.val)
            else:
                self.ans.append([root.val])
            self.levelOrderHelper(root.left, level + 1)
            self.levelOrderHelper(root.right, level + 1)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = self.levelOrderHelper(root)
        if ans and not ans[-1]:
            ans = ans[:-1]
        return ans
            
    def levelOrderHelper(self, root):
        if root is None:
            return [[]]
        else:
            ans = [[root.val]]
            left_ans = self.levelOrderHelper(root.left)
            right_ans = self.levelOrderHelper(root.right)
            rest = self.merge(left_ans, right_ans)
            #print('rest: %s' %str(rest))
            ans.extend(rest)
            #print('ans: %s' %str(ans))
            return ans
    
    def merge(self, left, right):
        #print('left: %s' %str(left))
        #print('right: %s' %str(right))
        
        while len(left) < len(right):
            left.append([])
            #print('pad left: %s' %str(left))
        while len(right) < len(left):
            right.append([])
            #print('pad right: %s' %str(right))
        
        for index in range(len(left)):
            left[index].extend(right[index])
        #print('result: %s' %str(left)) 
        return left

            
        
