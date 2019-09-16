from singleLinkList import *
class Solution(object):
    def partion(self, head, x):
        small_head = None
        small_tail = None
        big_head = None
        big_tail = None

        curr = head
        while curr:
            if curr.val < x:
                if small_head is None:
                    small_head = curr
                    small_tail = curr
                else:
                    small_tail.next = curr
                    small_tail = curr
            else:
                if big_head is None:
                    big_head = curr
                    big_tail = curr
                else:
                    big_tail.next = curr
                    big_tail = curr
            curr = curr.next

        #connect
        if big_tail:
            big_tail.next = None
        if small_tail:
            small_tail.next = big_head
            return small_head
        else:
            return big_head

if __name__ == '__main__':
    head = getALinkList()
    printLinkList(head)
    mySolution = Solution()
    part_head = mySolution.partion(head, 3)
    printLinkList(part_head)
    
