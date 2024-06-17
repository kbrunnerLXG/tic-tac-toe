class Board:
    def __init__(self) -> None:
        self.current_board = None

    def print_board(self):
        for row in self.current_board:
            print(" | ".join(row))
            print("-" * 9)

    def create_board(self):
        self.current_board = [[" " for _ in range(3)] for _ in range(3)]
        return self.current_board

    def board_out(self):
        return self.current_board
