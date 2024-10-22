# Tic-Tac-Toe Game in Python

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all([spot != ' ' for row in board for spot in row])

# Function to make a move
def make_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column: 1 1 for top-left): ").split()
        row, col = int(move[0]) - 1, int(move[1]) - 1

        if board[row][col] == ' ':
            board[row][col] = player
            break
        else:
            print("That spot is already taken. Try again.")

# Main function to run the game
def play_game():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Set up players
    current_player = 'X'

    # Game loop
    while True:
        print_board(board)
        make_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
