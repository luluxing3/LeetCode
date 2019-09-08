class Solution(object):
    def isValidRow(self, row):
        """
        :type row: List
        :rtype: bool
        """
        ele_set = set()
        for ele in row:
            if ele != '.':
                if ele not in ele_set:
                    ele_set.add(ele)
                else:
                    return False
        return True
        
    def get_col(self, board, i):
        """
        :type board: List[List[str]]
        :type i: int from 0 to len(board)-1
        :rtype: List
        """
        return [ row[i] for row in board ]
    
    def get_square(self, board, i, j):
        """
        :type i: int 0,1,2
        :type j: int 0,1,2
        :rtype: List
        """
        square = []
        for i in [3*i, 3*i+1, 3*i+2]:
            square.extend(board[i][j*3:(j+1)*3])
        return square
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isValidRow(row):
                return False
        for i in range(len(board)):
            col = self.get_col(board, i)
            if not self.isValidRow(col):
                return False
        for i in range(3):
            for j in range(3):
                square = self.get_square(board, i, j)
                if not self.isValidRow(square):
                    return False
        return True
                
