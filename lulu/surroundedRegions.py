class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        for i in range(len(board)):
            #first column
            if board[i][0] == 'O':
                board[i][0] = '+'
                self.bfs(i, 0, board)
                #print('first col')
            #last column
            if board[i][len(board[0]) - 1] == 'O':
                board[i][len(board[0]) - 1] = '+'
                self.bfs(i, len(board[0]) - 1, board)
                #print('last col')
        for j in range(1, len(board[0]) - 1):
            #first row
            if board[0][j] == 'O':
                board[0][j] = '+'
                self.bfs(0, j, board)
                #print('first row')
            if board[len(board) - 1][j] == 'O':
                board[len(board) - 1][j] = '+'
                self.bfs(len(board) - 1, j, board)
                #print('last row')

        #capture
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '+':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

    def isValid(self, i, j, board):
        nrow = len(board)
        ncol = len(board[0])
        return i >= 0 and i < nrow and j >=0 and j < ncol and board[i][j] == 'O'

    def bfs(self, i, j, board):
        newState = [(i-1, j), (i,j-1), (i, j+1), (i+1, j)]
        for (n_i, n_j) in newState:
            if self.isValid(n_i, n_j, board):
                board[n_i][n_j] = '+'
                self.bfs(n_i, n_j, board)
