class Solution(object):
    def longest(self, string):
        start = None
        maxLen = 0
        polindromicMatrix = [[None]*len(string) for x in range(len(string))]
        for i in range(len(string)):
            for j in range(i, len(string)):
                if i == j:
                    polindromicMatrix[i][j] = True
                elif j = i + 1:
                    polindromicMatrix[i][j] = string[i] == string[j]
                else:
                    polindromicMatrix[i][j] = (A[i]== A[j]) & polindromicMatrix[i+1][j-1]

                if polindromicMatrix[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i
        return string[i: i + maxLen]

