class Solution(object):
    def remove(self, head, n):
        if head is None:
            return
        p = head
        q = head
        count = 1
        while p and count != n+1:
            p = p.next
            count += 1
        
        if p is None:
            return head.next
        else:
            while p and p.next:
                p = p.next
                q = q.next
            

            q.next = q.next.next
            return head
        
