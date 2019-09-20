class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

def printList(head):
    curr = head
    string = ''
    while curr:
        if curr.next:
            next_val = curr.next.val
        else:
            next_val = None
        if curr.random:
            random_val = curr.random.val
        else:
            random_val = None
        string += '|val: %s, next: %s, random: %s|' %(curr.val, next_val, random_val) + '->'
        curr = curr.next
    string += 'NULL' 
    print(string)

def getAList():
    head = ListNode(0)
    tail = head
    for i in range(1, 5):
        newNode = ListNode(i)
        tail.next = newNode
        tail = newNode

    head.random = head.next.next.next
    head.next.random = head
    head.next.next.random = head.next
    printList(head)
    return head
    
class Solution(object):
    def copy(self, head):
        copy_head = None
        copy_tail = None
        hash_map = {}
        curr = head
        while curr:
            newNode = ListNode(curr.val)
            newNode.random = curr.random
            hash_map[curr] = newNode
            newNode.next = curr.next
            if copy_head:
                copy_tail.next = newNode
                copy_tail = copy_tail.next
            else:
                copy_head = newNode
                copy_tail = newNode
            curr = curr.next

        curr = copy_head
        while curr:
            if curr.random:
                curr.random = hash_map[curr.random]
            curr = curr.next

        return copy_head

    def copyNoHash(self, head):
        if head is None:
            return None
        curr = head
        while curr:
            newNode = ListNode(curr.val)
            newNode.random = curr.random
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        printList(head)

        q = head.next
        while q:
            if q.random:
                q.random = q.random.next
            if q.next:
                q = q.next.next
            else:
                break
        p = head
        q = head.next
        copy_head = head.next
        while q and q.next:
            p.next = p.next.next
            q.next = q.next.next
            p = p.next
            q = q.next
        p.next = None
        return copy_head

if __name__ == '__main__':
    head = getAList()
    mySolution = Solution()
    copy = mySolution.copyNoHash(head)
    print('original....')
    printList(head)
    print('copy....')
    printList(copy)


            
        


            
            
        
