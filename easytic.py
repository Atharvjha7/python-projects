import random
'''This is the easy level computer of the game I made in finalticgame.py using only random choice of the legal spaces to move in to play
Includes basic functionalities such as illegal move handling and other illegal input detection.
After this, I tested the performance of the computer at easytest.py All three computer players I made use no data but rather simple logic to ensure the best chance of winning for the given skillset'''
# Initialize the Tic Tac Toe board
board = [' '] * 9
player_marker = 'X'
computer_marker = 'O'

# Function to print the Tic Tac Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a win
def check_win(board, marker):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == marker for i in combo):
            return True
    return False

# Function to check for a tie
def check_tie(board):
    return ' ' not in board

# Function for the computer's move
def computer_move(board, marker):
    available_moves = [i for i, val in enumerate(board) if val == ' ']
    return random.choice(available_moves)

# Randomly decide who goes first
if random.choice([True, False]):
    print("Computer goes first.")
    computer_move_index = computer_move(board, computer_marker)
    board[computer_move_index] = computer_marker
else:
    print("You go first.")

# Main game loop
while True:
    print_board(board)

    # Human player's move
    while True:
        try:
            player_move = int(input("Enter your move (0-8): "))
            if 0 <= player_move <= 8 and board[player_move] == ' ':
                board[player_move] = player_marker
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Check if the human player wins or there's a tie
    if check_win(board, player_marker):
        print_board(board)
        print("Congratulations! You win!")
        break
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        break

    # Computer's move
    computer_move_index = computer_move(board, computer_marker)
    board[computer_move_index] = computer_marker

    # Check if the computer wins or there's a tie
    if check_win(board, computer_marker):
        print_board(board)
        print("Computer wins! Better luck next time.")
        break
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        break
