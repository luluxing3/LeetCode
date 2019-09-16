class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printLinkList(l):
    string = ''
    curr = l
    while curr:
        string += str(curr.val) + '->'
        curr = curr.next
    string += 'NULL'
    print(string)

def getALinkList():
    head = None
    for i in range(1, 10):
        if i % 2 == 0:
            newNode = ListNode(i)
            newNode.next = head
            head = newNode
        newNode = ListNode(i)
        newNode.next = head
        head = newNode
    printLinkList(head)
    return head

        
        
        

	
