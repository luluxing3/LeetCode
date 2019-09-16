from singleLinkList import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #l1_reverse = self.reverse(l1)
        #l2_reverse = self.reverse(l2)
        h1 = l1
        h2 = l2
        sumNode = None
        tail = None
        addOne = 0
        while h1 or h2:
            if h1:
                val1 = h1.val
            else:
                val1 = 0
            if h2:
                val2 = h2.val
            else:
                val2 = 0
            val = val1 + val2 + addOne
            if val >= 10:
                val = val - 10
                addOne = 1
            else:
                addOne = 0
            
            newNode = ListNode(val)
            if sumNode is None and tail is None:
                sumNode = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next
        if addOne == 1:
            newNode = ListNode(1)
            tail.next = newNode
            
        #printLinkList(sumNode)
        return sumNode

    def reverse(self, l):
        prev = None
        curr = l
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


if __name__ == '__main__':
    l1 = getALinkList()
    l2 = getALinkList()
    mySolution = Solution()
    #l1_reverse = mySolution.reverse(l1)
    #printLinkList(l1_reverse)
    result = mySolution.addTwoNumbers(l1, l2)
    #printLinkList(result)

