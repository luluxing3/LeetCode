from singleLinkList import *
class Solution(object):
    def rotate(self, head, k):
        #get length
        curr = head
        length = 0
        prev = None
        while curr:
            length += 1
            prev = curr
            curr = curr.next

        if length <= 1:
            return head

        #connect to a ring
        prev.next = head

        #cut
        count = 0
        curr = head
        k = k % length
        while count != length - k:
            prev = prev.next
            curr = curr.next
            count += 1
        prev.next = None
        rotate_head = curr
        return rotate_head


if __name__ == '__main__':
    head = getALinkList()
    mySolution = Solution()
    head = mySolution.rotate(head, k=22)
    printLinkList(head)
            

