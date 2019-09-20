from singleLinkList import *
class Solution(object):
    def reorder(self, head):
        if head is None or head.next is None:
            return
        meddle = self.getCenter(head)
        #print('meddle val: %s' %meddle.val)
        tail_part = self.reverse(meddle.next)
        #printLinkList(tail_part)
        meddle.next = None

        p = head
        q = tail_part  #head_part >= tail_part
        reorder_head = None
        reorder_tail = None
        while q:
            assert p is not None
            tmp_p = p.next
            tmp_q = q.next
            p.next = q
            if reorder_head:
                reorder_tail.next = p
                reorder_tail = q
            else:
                reorder_head = p
                reorder_tail = q

            p = tmp_p
            q = tmp_q
        if p:
            if reorder_tail:
                reorder_tail.next = p
            else:
                return p
        return reorder_head
    def getCenter(self, head):
        fast = head
        base = head
        while fast and fast.next:
            fast = fast.next.next
            base = base.next
        return base

    def reverse(self, head):
        if head is None:
            return None
        prev = None
        curr = head
        while curr and curr.next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        curr.next = prev
        return curr

if __name__ == '__main__':
    head = getALinkList()
    mySolution = Solution()
    head = mySolution.reorder(head)
    printLinkList(head)

