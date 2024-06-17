class Checker:
    def __init__(self) -> None:
        pass
    def check_win(self,board, player):
        # Check rows
        for row in board:
            if all(s == player for s in row):
                return True
        # Check columns
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False
    def check_draw(self,board):
        return all(cell != " " for row in board for cell in row)