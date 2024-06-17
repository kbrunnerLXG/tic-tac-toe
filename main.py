from board import Board
from chance import Chance
from check import Checker


def main():
    current_board = Board()
    current_board.create_board()
    chance = Chance()
    check = Checker()
    current_player = "X"
    while True:
        current_board.print_board(current_board.board)
        chance.get_move(current_board.board, current_player)
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
