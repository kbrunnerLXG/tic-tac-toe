class Chance:
    def __init__(self) -> None:
        self.current_player = 'X'

    def get_move(self, board):
        while True:
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = self.current_player
                    break
                else:
                    print("This spot is already taken!")
            except (ValueError, IndexError):
                print("Invalid move. Please enter a number between 1 and 9.")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
