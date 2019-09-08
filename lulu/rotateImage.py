class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 
        for i in range(len(matrix)):
            print(matrix[i])
        
        n = len(matrix)
        for i in range(n):
            for j in range(n-1-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        print('fisrt change')
        for i in range(len(matrix)):
            print(matrix[i])
        for i in range(n/2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        print('second change')
        for i in range(len(matrix)):
            print(matrix[i])


if __name__ == '__main__':
    mySolution = Solution()
    input_matrix = [
                      [1,2,3],
                      [4,5,6],
                      [7,8,9]
                   ]
    mySolution.rotate(input_matrix)
    input_matrix = [[1]]
    mySolution.rotate(input_matrix)
    input_matrix = []
    mySolution.rotate(input_matrix)
    input_matrix = [
                      [1,2,3,4],
                      [4,5,6,7],
                      [7,8,9,0],
                      [5,8,9,0]
                   ]
    mySolution.rotate(input_matrix)


    
