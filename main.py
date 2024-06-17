from board import Board
from chance import Chance
from check import Checker


def main():
    board = Board()
    board.create_board()
    chance = Chance()
    check = Checker()
    # current_player = "X"
    while True:
        board.print_board()
        chance.get_move(board.current_board)
        if check.check_win(board.current_board, chance.current_player):
            board.print_board()
            print(f"Player {chance.current_player} wins!")
            break
        elif check.check_draw(board.current_board):
            board.print_board()
            print("The game is a draw!")
            break
        # Switch player
        chance.switch_player()


if __name__ == "__main__":
    main()
