class Solution(object):
    def longest(self, string):
        start = None
        maxLen = 0
        polindromicMatrix = [[None]*len(string) for x in range(len(string))]
        for j in range(len(string)):
            for i in range(len(string)):
                if j == 0:
                    polindromicMatrix[i][i+j] == True
                elif j == 1:
                    if i + j < len(string):
                        polindromicMatrix[i][i+j] = string[i] == string[i+j]
                else:
                    if i + j < len(string):
                        polindromicMatrix[i][i+j] = (string[i] == string[i+j]) and polindromicMatrix[i+1][j-1]

                if i + j < len(string) and polindromicMatrix and j+1 > maxLen:
                    start = i
                    maxLen = j + 1
          return string[start: start + maxLen]
                    
                    


