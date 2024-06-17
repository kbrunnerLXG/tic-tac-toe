class Player:
    def __init__(self) -> None:
        pass

    def get_move(self, board, player):
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("This spot is already taken!")
            except (ValueError, IndexError):
                print("Invalid move. Please enter a number between 1 and 9.")