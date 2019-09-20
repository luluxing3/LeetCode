class Solution(object):
    def roman2Int(self, string):
        if not string:
            return 0
        hash_table = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        #radix = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        #symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        if len(string) >= 2 and string[:2] in hash_table:
            return hash_table[string[:2]] + self.roman2Int(string[2:])
        else:
            assert string[0] in hash_table
            return hash_table[string[0]] + self.roman2Int(string[1:])


if __name__ == '__main__':
    mySolution = Solution()
    print('%s\t%s\t%s' %(39, 'XXXIX', mySolution.roman2Int('XXXIX')))
    print('%s\t%s\t%s' %(246, 'CCXLVI', mySolution.roman2Int('CCXLVI')))
        


        
