from board import Board
from chance import Chance
from check import Checker


def main():
    board = Board()
    board.create_board()
    chance = Chance()
    check = Checker()
    current_player = "X"
    while True:
        board.print_board()
        chance.get_move(board.current_board, current_player)
        if check.check_win(board.current_board, current_player):
            board.print_board()
            print(f"Player {current_player} wins!")
            break
        elif check.check_draw(board.current_board):
            board.print_board()
            print("The game is a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
