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
				return True
		return False

