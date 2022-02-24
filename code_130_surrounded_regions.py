class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        
        n = len(board)
        m = len(board[0])
        
        ignore = [_ for x in range(m+n) for _ in ((0,x),(n-1,x),(x,0),(x,m-1))]
        while ignore:
            row, col = ignore.pop()
            if 0 <= row < n and 0 <= col < m and board[row][col] == 'O':
                board[row][col] = 'IGNORE'
                ignore += (row, col-1), (row, col+1), (row-1,col), (row+1,col)

        board[:] = [['XO' [c == 'IGNORE'] for c in row] for row in board]