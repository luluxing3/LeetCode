from singleLinkList import *
class Solution(object):
    def reverseGroup(self, head, k):
        if head is None or head.next is None:
            return head
        start = head
        tail = head
        count = 1
        while tail and tail.next and count != k:
            tail = tail.next
            count += 1
        if count != k:
            return head
        else:
            tmp = tail.next
            #print('start val: %s\t tail val: %s' %(start.val, tail.val))
            start, tail = self.reverse(start, tail)
            #print('start val: %s\t tail val: %s' %(start.val, tail.val))
            tail.next = self.reverseGroup(tmp, k)
            return start

    def reverse(self, start, tail):
        #start and tail is not None
        prev = None
        curr = start
        while curr is not tail:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tail.next = prev
        return tail, start
    
if __name__ == '__main__':
    head = getALinkList()
    mySolution = Solution()
    head = mySolution.reverseGroup(head, k=3)
    printLinkList(head)
