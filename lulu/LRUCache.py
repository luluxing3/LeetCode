class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.head = None
        self.tail = None
        self.hash_table = {} #key->pointer

    def deleteTail(self):
        if self.count == 0:
            return
        elif self.count == 1:
            assert self.head
            del self.hash_table[self.head.key]
            self.head = None
            self.tail = None
            self.count -= 1
        else:
            assert self.tail
            assert self.tail.prev 
            del self.hash_table[self.tail.key]
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1

    def addHead(self, key, value):
        newNode = ListNode(key, value)
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:
            assert self.head
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.count += 1
        self.hash_table[key] = newNode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_table:
            p = self.hash_table[key]

            #swape to head
            assert p
            assert self.head
            if p is self.head:
                return p.value
            else:
                assert p.prev
                if p is self.tail:
                    #update tail
                    self.tail = p.prev
                    self.tail.next = None
                else:
                    #delete p
                    assert p.next
                    p.prev.next = p.next
                    p.next.prev = p.prev
            
                #update head
                p.prev = None
                p.next = self.head
                self.head.prev = p
                self.head = p
                return p.value
        else:
            return -1
               
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash_table:
            p = self.hash_table[key]
            if p is self.tail:
                self.deleteTail()
            elif p is self.head:
                self.hash_table[key].value = value
                return
            else:
                #delete p
                assert p.next
                assert p.prev
                p.prev.next = p.next
                p.next.prev = p.prev
                self.count -= 1
        if self.count == self.capacity:
            self.deleteTail()
        self.addHead(key, value)
        ##print('before put----')
        ##self.myPrint()
        ##print('before put---')
        #if key in self.hash_table:
        #    return 

        #newNode = ListNode(key, value)
        #self.hash_table[key] = newNode
        #if self.count == 0:
        #    self.head = newNode
        #    self.tail = newNode
        #    #self.hash_table[key] = newNode
        #    self.count += 1
        #elif self.count < self.capacity:
        #    #insert newNode at head
        #    assert self.head
        #    self.head.prev = newNode
        #    newNode.next = self.head
        #    self.head = newNode

        #    #self.hash_table[key] = newNode
        #    self.count += 1
        #else:
        #    #print('---debug---')
        #    #self.myPrint()
        #    #print('---debug---')

        #    #delete tail
        #    assert self.tail
        #    del self.hash_table[self.tail.key]
        #    #self.hash_table[key] = newNode
        #    self.tail = self.tail.prev
        #    if self.tail:
        #        #when capacity is 1, self.tail is None
        #        self.tail.next = None
        #        assert self.head
        #        self.head.prev = newNode
        #        newNode.next = self.head
        #        self.head = newNode
        #    else:
        #        self.head = None
        #        self.head = newNode
        #        self.tail = newNode

        #    #print('---debug---')
        #    #self.myPrint()
        #    #print('---debug---')

        #    #add newNode to head
        #    newNode.next = self.head
        #    self.head.prev = newNode
        #    self.head = newNode
        #    self.hash_table[key] = newNode

    def myPrint(self):
        print('-'*10)
        print('count = %s' %self.count)
        if self.head:
            head_val = self.head.value
        else: 
            head_val = None
        print('head: %s' %head_val)
        if self.tail:
            tail_val = self.tail.value
        else:
            tail_val = None
        print('tail: %s' %tail_val)
        curr = self.head
        string = ''
        while curr:
            string += str(curr.value) + '->'
            curr = curr.next
        string += 'NULL'
        print(string)
        prev_string = 'NULL'
        curr = self.tail
        while curr:
            prev_string = str(curr.value) + '<-' + prev_string
            curr = curr.prev
        print(prev_string)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    #obj = LRUCache(2)
    #obj.myPrint()
    ##print('expect: -1\t %s' %obj.get(1))
    #for i in range(7):
    #    print('---%s--' %i)
    #    obj.put(i, i)
    #    #obj.addHead(i, i)
    #    obj.myPrint()
    #    print(obj.get(1))
    #    obj.myPrint()
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.myPrint()
    obj.put(2, 2)
    obj.myPrint()
    print('***'+ str(obj.get(2)))
    obj.myPrint()
    obj.put(1, 1)
    obj.myPrint()
    obj.put(4, 1)
    obj.myPrint()
    print('***'+str(obj.get(2)))
    obj.myPrint()

    
