import random
''' Test of 1000 randomly simulated games that are outputted for the best computer player/level of the three, if you haven't already, visit my inital ones at easytic.py and mediumtic.py 
to see their performance and structure.'''
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

# Function to find the next move for the computer
def computer_move(board, computer_marker, player_marker):
    # Check for a win
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer_marker
            if check_win(board, computer_marker):
                return i
            else:
                board[i] = ' '

    # Block the player from winning
    for i in range(9):
        if board[i] == ' ':
            board[i] = player_marker
            if check_win(board, player_marker):
                return i
            else:
                board[i] = ' '

    # Fork opportunity for the computer
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer_marker
            fork_possible = False
            for j in range(9):
                if board[j] == ' ':
                    board[j] = computer_marker
                    if check_win(board, computer_marker):
                        fork_possible = True
                    board[j] = ' '
            if fork_possible:
                return i
            else:
                board[i] = ' '

    # Block the player's fork attempt
    for i in range(9):
        if board[i] == ' ':
            board[i] = player_marker
            fork_possible = False
            for j in range(9):
                if board[j] == ' ':
                    board[j] = player_marker
                    if check_win(board, player_marker):
                        fork_possible = True
                    board[j] = ' '
            if fork_possible:
                return i
            else:
                board[i] = ' '

    # Try to take the center
    if board[4] == ' ':
        return 4

    # Try to take a corner
    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for corner in corners:
        if board[corner] == ' ':
            return corner

    # Take any available edge
    edges = [1, 3, 5, 7]
    random.shuffle(edges)
    for edge in edges:
        if board[edge] == ' ':
            return edge

# Function to play a single game
def play_game():
    # Initialize the Tic Tac Toe board
    board = [' '] * 9
    player_marker = 'X'
    computer_marker = 'O'

    # Randomly decide who goes first
    if random.choice([True, False]):
        current_player = "AI"
    else:
        current_player = "Random Computer"

    while True:
        if current_player == "AI":
            computer_move_index = computer_move(board, computer_marker, player_marker)
            board[computer_move_index] = computer_marker
            if check_win(board, computer_marker):
                return "AI"
            elif check_tie(board):
                return "Tie"
            current_player = "Random Computer"
        else:
            available_moves = [i for i, val in enumerate(board) if val == ' ']
            if not available_moves:
                return "Tie"
            random_move = random.choice(available_moves)
            board[random_move] = player_marker
            if check_win(board, player_marker):
                return "Random Computer"
            elif check_tie(board):
                return "Tie"
            current_player = "AI"

# Play 1,000 games and keep track of results
ai_wins = 0
random_computer_wins = 0
ties = 0

for _ in range(1000):
    result = play_game()
    if result == "AI":
        ai_wins += 1
    elif result == "Random Computer":
        random_computer_wins += 1
    else:
        ties += 1

# Print the results
print(f"AI wins: {ai_wins}")
print(f"Random Computer wins: {random_computer_wins}")
print(f"Ties: {ties}")
