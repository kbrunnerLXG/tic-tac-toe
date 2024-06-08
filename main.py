from board import Board
tic_tac_board = Board()
board = tic_tac_board.make_board()
winner_found = False
i = 0
while not winner_found:
    if i == 0:
        beginning = True
        tic_tac_board.start_game(beginning, board)
        i += 1
    else:
        beginning = False
        tic_tac_board.start_game(beginning, board)
        i += 1
