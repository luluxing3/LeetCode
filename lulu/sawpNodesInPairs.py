class Solution(object):
    def swap(self, head):
        if head is None or head.next is None:
            return head
        head_swap = head.next
        tmp = head_swap.next
        head_swap.next = head
        head.next = self.swap(tmp)
        return head_swap

