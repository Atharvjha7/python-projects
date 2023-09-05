'''This is a tic-tac-toe game that provides a two player option or a user against varying levels of a computer 
To see the code and performance tests for each level, check the other projects in this rep that have comments to guide you where to go'''
import random

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

# Function to find the next move for the computer (random)
def random_computer_move(board):
    available_moves = [i for i, val in enumerate(board) if val == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None

# Function to find the next move for the computer (less advanced)
def less_advanced_ai_move(board):
    # Implement your less advanced AI strategy here
    # For now, use random move
    return random_computer_move(board)

# Function to find the next move for the computer (advanced)
def advanced_ai_move(board, computer_marker, player_marker):
    # Implement your advanced AI strategy here
    # For now, use random move
    return random_computer_move(board)

# Function to simulate a game against the chosen AI level
def play_game(ai_level):
    # Initialize the Tic Tac Toe board
    board = [' '] * 9
    player_marker = 'X'
    computer_marker = 'O'

    print_board(board)

    while True:
        if ai_level == 'random':
            computer_move_index = random_computer_move(board)
        elif ai_level == 'less_advanced':
            computer_move_index = less_advanced_ai_move(board)
        elif ai_level == 'advanced':
            computer_move_index = advanced_ai_move(board, computer_marker, player_marker)
        else:
            print("Invalid AI level.")
            return

        if computer_move_index is not None:
            board[computer_move_index] = computer_marker

        print_board(board)

        # Check if the computer wins or there's a tie
        if check_win(board, computer_marker):
            print("Computer wins! Better luck next time.")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

        # Player's move
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

        print_board(board)

        # Check if the player wins or there's a tie
        if check_win(board, player_marker):
            print("Congratulations! You win!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

# Function to get the next move from a player
def get_player_move(board, marker):
    while True:
        try:
            player_move = int(input(f"Player {marker}, enter your move (0-8): "))
            if 0 <= player_move <= 8 and board[player_move] == ' ':
                return player_move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to simulate a game between two players
def play_two_player_game():
    # Initialize the Tic Tac Toe board
    board = [' '] * 9
    players = ['X', 'O']
    current_player_index = 0

    print_board(board)

    while True:
        current_player = players[current_player_index]

        player_move = get_player_move(board, current_player)
        board[player_move] = current_player

        print_board(board)

        # Check if the current player wins or there's a tie
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print("It's a tie!")
            break

        # Switch to the other player
        current_player_index = (current_player_index + 1) % 2

# Main function to run the game
def main():
    print("Welcome to Tic Tac Toe!")

    while True:
        print("Choose a game mode:")
        print("1. Play against AI")
        print("2. Two players")
        print("3. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("Choose the AI difficulty level:")
            print("1. Random AI")
            print("2. Less Advanced AI")
            print("3. Advanced AI")
            print("4. Back")
            ai_choice = input("Enter the number of your choice: ")
            if ai_choice == '1':
                play_game('random')
            elif ai_choice == '2':
                play_game('less_advanced')
            elif ai_choice == '3':
                play_game('advanced')
            elif ai_choice == '4':
                continue
            else:
                print("Invalid choice. Please enter a valid number.")
        elif choice == '2':
            play_two_player_game()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
