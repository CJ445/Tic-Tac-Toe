import tkinter as tk
from tkinter import ttk, messagebox
import math

# Define the game board
def create_board():
    return [' ' for _ in range(9)]

# Display the game board (in console for debugging purposes)
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
def play_game_single(player_name, scores, root, buttons, current_player_var):
    board = create_board()
    for button in buttons:
        button.config(text='', state=tk.NORMAL)
    current_player_var.set(f"{player_name}'s turn")

    def button_click(index):
        if human_move(board, index, 'O'):
            buttons[index].config(text='O', state=tk.DISABLED)
            winner = check_winner(board)
            if winner:
                if winner == 'Draw':
                    messagebox.showinfo("Game Over", "The game is a draw!")
                else:
                    messagebox.showinfo("Game Over", f"The winner is {winner}!")
                update_scores(winner, scores, player_name, root)
                return
            ai_move = get_best_move(board)
            board[ai_move] = 'X'
            buttons[ai_move].config(text='X', state=tk.DISABLED)
            winner = check_winner(board)
            if winner:
                if winner == 'Draw':
                    messagebox.showinfo("Game Over", "The game is a draw!")
                else:
                    messagebox.showinfo("Game Over", f"The winner is {winner}!")
                update_scores(winner, scores, player_name, root)
                return

    for i, button in enumerate(buttons):
        button.config(command=lambda i=i: button_click(i))

# Main game loop for two players
def play_game_two_players(player1_name, player2_name, scores, root, buttons, current_player_var):
    board = create_board()
    for button in buttons:
        button.config(text='', state=tk.NORMAL)
    current_player = player1_name
    current_player_var.set(f"{current_player}'s turn")

    def button_click(index):
        nonlocal current_player
        player_symbol = 'X' if current_player == player1_name else 'O'
        if human_move(board, index, player_symbol):
            buttons[index].config(text=player_symbol, state=tk.DISABLED)
            winner = check_winner(board)
            if winner:
                if winner == 'Draw':
                    messagebox.showinfo("Game Over", "The game is a draw!")
                else:
                    messagebox.showinfo("Game Over", f"The winner is {winner} ({current_player})!")
                update_scores(winner, scores, player1_name, root, player2_name)
                return
            current_player = player2_name if current_player == player1_name else player1_name
            current_player_var.set(f"{current_player}'s turn")

    for i, button in enumerate(buttons):
        button.config(command=lambda i=i: button_click(i))

def update_scores(winner, scores, player1_name, root, player2_name=None):
    if winner == 'X':
        scores['AI' if player2_name is None else player1_name] += 1
    elif winner == 'O':
        scores[player1_name if player2_name is None else player2_name] += 1
    elif winner == 'Draw':
        pass
    show_scores(scores, player1_name, root, player2_name)

def show_scores(scores, player_name, root, player2_name=None):
    score_text = f"Scores:\nAI: {scores['AI']}\n{player_name}: {scores[player_name]}"
    if player2_name:
        score_text += f"\n{player2_name}: {scores[player2_name]}"
    messagebox.showinfo("Scores", score_text)

def main():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    
    # Set up styling
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 14))
    style.configure("TLabel", font=("Helvetica", 14))
    
    scores = {'AI': 0}
    player_name = tk.StringVar()
    player2_name = tk.StringVar()
    current_player_var = tk.StringVar()
    
    def start_single_player_game():
        name = player_name.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if name not in scores:
            scores[name] = 0
        play_game_single(name, scores, root, buttons, current_player_var)

    def start_two_player_game():
        name1 = player_name.get()
        name2 = player2_name.get()
        if not name1 or not name2:
            messagebox.showerror("Error", "Please enter both players' names.")
            return
        if name1 not in scores:
            scores[name1] = 0
        if name2 not in scores:
            scores[name2] = 0
        play_game_two_players(name1, name2, scores, root, buttons, current_player_var)

    def on_exit():
        root.destroy()

    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky="NSEW")
    
    ttk.Label(main_frame, text="Player 1 Name:").grid(row=0, column=0, pady=5)
    ttk.Entry(main_frame, textvariable=player_name, width=20).grid(row=0, column=1, pady=5)
    ttk.Label(main_frame, text="Player 2 Name:").grid(row=1, column=0, pady=5)
    ttk.Entry(main_frame, textvariable=player2_name, width=20).grid(row=1, column=1, pady=5)
    
    ttk.Button(main_frame, text="Start Single Player Game", command=start_single_player_game).grid(row=2, column=0, columnspan=2, pady=10)
    ttk.Button(main_frame, text="Start Two Player Game", command=start_two_player_game).grid(row=3, column=0, columnspan=2, pady=10)
    ttk.Button(main_frame, text="View Scores", command=lambda: show_scores(scores, player_name.get(), root, player2_name.get())).grid(row=4, column=0, columnspan=2, pady=10)
    ttk.Button(main_frame, text="Exit", command=on_exit).grid(row=5, column=0, columnspan=2, pady=10)
    
    buttons_frame = ttk.Frame(main_frame, padding="10")
    buttons_frame.grid(row=6, column=0, columnspan=2, pady=10)
    
    buttons = []
    for i in range(9):
        button = ttk.Button(buttons_frame, text='', width=10, style="TButton")
        button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        buttons.append(button)

    ttk.Label(main_frame, textvariable=current_player_var).grid(row=7, column=0, columnspan=2, pady=10)

    root.mainloop()

# Start the game
main()
