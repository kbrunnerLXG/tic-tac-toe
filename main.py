from board import Board
from player import Player
from check import Checker


def get_move(board, player):
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


def main():
    current_board = Board()
    current_board.create_board()
    check = Checker()
    current_player = "X"
    while True:
        current_board.print_board(current_board.board)
        get_move(current_board.board, current_player)
        if check.check_win(current_board.board, current_player):
            current_board.print_board(current_board.board)
            print(f"Player {current_player} wins!")
            break
        elif check.check_draw(current_board.board):
            current_board.print_board(current_board.board)
            print("The game is a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
