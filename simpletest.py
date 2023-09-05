import random

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

# Function to find the next move for the computer (less advanced version)
def computer_move(board, computer_marker):
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            return move

# Function to print the Tic Tac Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Main game loop 
def main():
    # Initialize the Tic Tac Toe board
    board = [' '] * 9
    player_marker = 'X'
    computer_marker = 'O'

    print("Computer goes first.")

    while True:
        print_board(board)

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

if __name__ == "__main__":
    main()
