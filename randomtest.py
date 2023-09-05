import random
''' This is a test of the random computer tic tac toe player I made in randomtictac.py, I am using 1000 random simulated games and outputting the results after. I made a non-random, improved version of this
over in simpletictac.py .'''
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
def computer_move(board):
    available_moves = [i for i, val in enumerate(board) if val == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None

# Function to simulate a random game
def simulate_random_game():
    board = [' '] * 9
    player_marker = 'X'
    computer_marker = 'O'

    # Randomly decide who goes first
    if random.choice([True, False]):
        computer_move_index = computer_move(board)
        board[computer_move_index] = computer_marker

    while True:
        # Player's move
        player_move = random.choice([i for i, val in enumerate(board) if val == ' '])
        board[player_move] = player_marker

        # Check if the player wins or there's a tie
        if check_win(board, player_marker):
            return 'player'
        elif check_tie(board):
            return 'tie'

        # Computer's move
        computer_move_index = computer_move(board)
        if computer_move_index is not None:
            board[computer_move_index] = computer_marker

        # Check if the computer wins or there's a tie
        if check_win(board, computer_marker):
            return 'computer'
        elif check_tie(board):
            return 'tie'

# Function to simulate multiple random games and count results
def simulate_random_games(num_games):
    results = {'player': 0, 'computer': 0, 'tie': 0}

    for _ in range(num_games):
        winner = simulate_random_game()
        results[winner] += 1

    return results

# Main function to run the simulation
def main():
    num_games = 1000

    print(f"Simulating {num_games} random games...")
    results = simulate_random_games(num_games)

    print("\nResults:")
    print(f"Player wins: {results['player']} times")
    print(f"Computer wins: {results['computer']} times")
    print(f"Ties: {results['tie']} times")

if __name__ == "__main__":
    main()
