from singleLinkList import *
class Solution(object):
    def remove(self, head):
        prev = None
        curr = head
        while curr:
            if prev and prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head

    def removeRecursive(self, head):
        if head is None or head.next is None:
            return head

        curr = head.next
        while curr and curr.val == head.val:
            curr = curr.next

        head.next = self.removeRecursive(curr)
        return head

if __name__ == '__main__':
    head = getALinkList()
    printLinkList(head)
    mySolution = Solution()
    remove_head = mySolution.removeRecursive(head)
    printLinkList(remove_head)
    
