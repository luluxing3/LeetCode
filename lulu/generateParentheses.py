class Solution(object):
    def generate(self, n):
        if n == 1:
            return ['()']
        else:
            ans = set()
            for rest in self.generate(n - 1):
                ans.add(rest + '()')
                ans.add('(' + rest + ')')
                ans.add('()' + rest)
            return list(ans)

class Solution(object):
    def __init__(self):
        self.ans = []

    def generate(self, n):
        self.generateHelper('', 0, 0, n)
        return self.ans

    def generateHelper(self, s, left, right, n):
        if len(s) == 2 * n:
            self.ans.append(s)
            return
        if left < n:
            self.generateHelper(s + '(', left + 1, right, n)
        if right < left:
            self.generateHelper(s + ')', left, right + 1, n)


