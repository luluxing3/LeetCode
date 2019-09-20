class Solution(object):
    def say(self, string):
        lastNum = ''
        count = 0
        sayWords = ''
        for n in string:
            if lastNum == n:
                count += 1
            else:
                if count and lastNum:
                    sayWords += str(count) + lastNum
                lastNum = n
                count = 1

        if count and lastNum:
            sayWords += str(count) + lastNum
        return sayWords

    def sayAndCount(self, n):
        string = '1'
        for i in range(1, n):
            string = self.say(string)
        return string


if __name__ == '__main__':
    mySolution = Solution()
    for n in range(1, 10):
        print(mySolution.sayAndCount(n))
        
                 

        
