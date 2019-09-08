class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 
        isFirstRowZeros = 0 in matrix[0]
        isFirstColumnZeros = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isFirstColumnZeros = True
            
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                self.setRowZeros(matrix, i)
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                self.setColumnZeros(matrix, j)
        if isFirstRowZeros:
            self.setRowZeros(matrix, 0)
        if isFirstColumnZeros:
            self.setColumnZeros(matrix, 0)

    def setRowZeros(self, matrix, i):
        matrix[i] = [0] * len(matrix[i])

    def setColumnZeros(self, matrix, j):
        for i in range(len(matrix)):
            matrix[i][j] = 0

    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            print(matrix[i])
        print('-'*5)


if __name__ == '__main__':
    input_matrix = [
                      [0,2,3,5],
                      [4,0,6,7],
                      [7,8,9,8]
                   ]
    mySolution = Solution()
    mySolution.printMatrix(input_matrix)
    mySolution.setZeroes(input_matrix)
    mySolution.printMatrix(input_matrix)
    print('='*20)
    input_matrix = [[1,0]]
    mySolution.printMatrix(input_matrix)
    mySolution.setZeroes(input_matrix)
    mySolution.printMatrix(input_matrix)
    input_matrix = [[1,1,1],[0,1,2]]
    print('='*20)
    mySolution.printMatrix(input_matrix)
    mySolution.setZeroes(input_matrix)
    mySolution.printMatrix(input_matrix)

    
