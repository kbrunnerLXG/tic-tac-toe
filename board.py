class Board:
    def __init__(self) -> None:
        self.board = None
        return self.board

    def print_board(self, board):
        for row in board:
            print(" | ".join(row))
            print("-" * 9)

    def create_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        return self.board

    def board_out(self):
        return self.board
