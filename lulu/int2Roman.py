class Solution(object):
    def int2Roman(self, num):
        radix = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        Roman = ''
        while num:
            count = num / radix[i]
            num = num % radix[i]
            Roman += symbol[i] * count
            i += 1
        return Roman


if __name__ == '__main__':
    mySolution = Solution()
    print('%s\t%s' %(246, mySolution.int2Roman(246)))
    print('%s\t%s' %(709, mySolution.int2Roman(709)))
    print('%s\t%s' %(790, mySolution.int2Roman(790)))
    print('%s\t%s' %(789, mySolution.int2Roman(789)))
        


        
