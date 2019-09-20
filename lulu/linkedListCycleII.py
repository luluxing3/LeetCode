class Solution(object):
	def cycle(self, head):
		p = head
		q = head
		while p and p.next:
			#fast p
			p = p.next.next
			#slow q
			q = q.next

			if p == q:
                #collision
				return self.findStart(head, q)
		return None

    def findStart(self, head, collision):
        p = head
        q = collision
        while p != q:
            p = p.next
            q = q.next
        return p

