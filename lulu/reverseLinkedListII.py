from singleLinkList import *
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n or head is None:
            return head
        #head m
        prev = None
        count = 0
        while count != m-1:
            if prev is None:
                prev = head
            else:
                prev = prev.next
            count += 1

        if prev:
            start = prev.next
        else:
            start = head
        #reverse n-m times
        start_reverse = self.reverseTimes(start, n-m) 
        if prev:
            prev.next = start_reverse
        else:
            head = start_reverse

        return head

    def reverseTimes(self, start, n):
        prev = None
        curr = start
        count = 0
        while count != n+1:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            count += 1
        start.next = curr
        print('----reverse result---')
        printLinkList(prev)
        return prev

if __name__ == '__main__':
    l = getALinkList()
    printLinkList(l)
    mySolution = Solution()
    l = mySolution.reverseBetween(l, 1, 5)
    printLinkList(l)
    




