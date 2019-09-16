from singleLinkList import *
class Solution(object):
    def remove(self, head):
        remove_head = None
        remove_tail = None

        tmp_insert = head
        while tmp_insert:
            tmp_next = tmp_insert.next
            #print('----')
            #if tmp_next:
                #print('tmp_insert: %s tmp_next: %s' %(tmp_insert.val, tmp_next.val))
            if tmp_next is None:
                #final one
                if remove_tail:
                    remove_tail.next = tmp_insert
                    break
                else:
                    remove_head = tmp_insert
                    break
            elif tmp_next.val != tmp_insert.val:
                #print('insert')
                if remove_head:
                    remove_tail.next = tmp_insert
                    remove_tail = tmp_insert
                else:
                    remove_head = tmp_insert
                    remove_tail = tmp_insert
                tmp_insert = tmp_next
            else:
                #print('**')
                while tmp_next and tmp_next.val == tmp_insert.val:
                    tmp_next = tmp_next.next
                    #print('tmp_insert: %s tmp_next: %s' %(tmp_insert.val, tmp_next.val))
                    
                tmp_insert = tmp_next
        if remove_tail:
            remove_tail.next = None
        return remove_head

    def removeRecursive(self, head):
        if head is None or head.next is None:
            return head

        remove_head = None
        remove_tail = None
        curr = head.next
        if curr and curr.val != head.val:
            if remove_head:
                remove_tail.next = head
                remove_tail = head
                remove_tail.next = self.removeRecursive(curr)
            else:
                remove_head = head
                remove_tail = head
                remove_tail.next = self.removeRecursive(curr)
        else:
            while curr and curr.val == head.val:
                curr = curr.next
            if remove_head:
                remove_tail.next = self.removeRecursive(curr)
            else:
                remove_head = self.removeRecursive(curr)

        return remove_head

if __name__ == '__main__':
    head = getALinkList()
    #printLinkList(head)
    mySolution = Solution()
    remove_head = mySolution.removeRecursive(head)
    printLinkList(remove_head)
    
