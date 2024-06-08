from user import User
from check import Check


def return_element(pos, board_tosech):
    element = {'value': board_tosech[int(pos[0]) - 1][int(pos[1]) - 1],
               'position': [int(pos[0]) - 1, int(pos[1]) - 1]}
    return element


def make_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board


def print_board(board):
    print('--look-below--')
    for row in board:
        print(row)
    print('--------------')


class Board:
    def __init__(self):
        self.player_1 = None
        self.player_2 = None
        self.pos = None
        self.board = None

    def make_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        return self.board

    def start_game(self, new_start, board1):
        if new_start:
            print('Welcome to the tic-tac-toe')
            print_board(board1)
        else:
            print_board(board1)
        self.player_1 = User(1)
        self.player_2 = User(2)
        self.make_a_mark(self.player_1, board1)
        self.make_a_mark(self.player_2, board1)

    def make_a_mark(self, player, board_inuse):
        global elementv_in_board, elementp_in_board
        self.pos = player.select_pos()
        try:
            element_in_board = return_element(self.pos, board_inuse)
            elementv_in_board = element_in_board['value']
            elementp_in_board = element_in_board['position']
        except IndexError:
            print('Invalid Position')
            return
        else:
            i, j = elementp_in_board[0], elementp_in_board[1]
            board_inuse[i][j] = player.player_mark_type
        finally:
            print_board(board_inuse)
