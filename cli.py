import math

# Define the game board
def create_board():
    return [' ' for _ in range(9)]

# Display the game board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check if there's a winner or the game is a draw
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    
    if ' ' not in board:
        return 'Draw'
    
    return None

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Draw': 0}
    result = check_winner(board)
    if result is not None:
        return scores[result]
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Get the best move for the AI
def get_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_value = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move

# Handle the human player's move
def human_move(board, move, player_symbol):
    if board[move] == ' ':
        board[move] = player_symbol
        return True
    return False

# Main game loop for single player
def play_game_single(player_name, scores):
    board = create_board()
    print_board(board)
    
    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if not human_move(board, move, 'O'):
            print("Invalid move. Try again.")
            continue
        
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("The game is a draw!")
            else:
                print(f"The winner is {winner}!")
            if winner == 'X':
                scores['AI'] += 1
            elif winner == 'O':
                scores[player_name] += 1
            break
        
        # AI move
        ai_move = get_best_move(board)
        board[ai_move] = 'X'
        print("AI move:")
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("The game is a draw!")
            else:
                print(f"The winner is {winner}!")
            if winner == 'X':
                scores['AI'] += 1
            elif winner == 'O':
                scores[player_name] += 1
            break

# Main game loop for two players
def play_game_two_players(player1_name, player2_name, scores):
    board = create_board()
    print_board(board)
    current_player = player1_name
    player_symbol = {'X': player1_name, 'O': player2_name}
    
    while True:
        # Current player move
        move = int(input(f"{current_player}, enter your move (1-9): ")) - 1
        if not human_move(board, move, 'X' if current_player == player1_name else 'O'):
            print("Invalid move. Try again.")
            continue
        
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Draw':
                print("The game is a draw!")
            else:
                print(f"The winner is {player_symbol[winner]}!")
            if winner == 'X':
                scores[player1_name] += 1
            elif winner == 'O':
                scores[player2_name] += 1
            break
        
        # Switch players
        current_player = player2_name if current_player == player1_name else player1_name

def main():
    scores = {'AI': 0}
    player_name = input("Enter your name: ")
    scores[player_name] = 0
    
    while True:
        print("\nMenu:")
        print("1. Start a new game (single player)")
        print("2. Start a new game (two players)")
        print("3. View scores")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            play_game_single(player_name, scores)
        elif choice == '2':
            player2_name = input("Enter the second player's name: ")
            if player2_name not in scores:
                scores[player2_name] = 0
            play_game_two_players(player_name, player2_name, scores)
        elif choice == '3':
            print(f"Scores: AI: {scores['AI']} | {player_name}: {scores[player_name]}")
            for player in scores:
                if player != 'AI' and player != player_name:
                    print(f"{player}: {scores[player]}")
        elif choice == '4':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the game
main()
