def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

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
    board = create_board()
    current_player = "X"
    
    while True:
        print_board(board)
        get_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()


