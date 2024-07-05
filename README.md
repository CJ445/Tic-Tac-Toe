# Project Title: Tic-Tac-Toe Game with GUI and CLI Options

## Project demo

### GUI mode
https://github.com/CJ445/Tic-Tac-Toe/assets/131938772/81f5fe05-40a7-42b7-ac5f-9664640250d9

### CLI mode
https://github.com/CJ445/Tic-Tac-Toe/assets/131938772/98ead21a-fcea-4a76-a6e6-e67e452160bd

## Project Description

This project implements a classic Tic-Tac-Toe game that offers two modes of play: a Graphical User Interface (GUI) version and a Command Line Interface (CLI) version. The game provides options for single-player mode against an AI opponent or two-player mode for human vs. human matches. Scores are tracked across sessions, and players can choose their preferred mode of interaction.

## Features

- **Single Player Mode**: Play against an unbeatable AI using the Minimax algorithm with Alpha-Beta pruning.
- **Two Player Mode**: Two human players can play against each other.
- **Score Tracking**: Keeps track of scores between sessions.
- **User-Friendly Interface**: Provides a choice between GUI and CLI for different user preferences.

## Files

### `gui.py`
Implements the Tic-Tac-Toe game using a graphical interface with `tkinter`.
- **Game Board**: Displayed using `ttk.Button` widgets.
- **Player Names**: Users can enter their names, which are displayed and used in the game.
- **Single Player Mode**: Play against an AI.
- **Two Player Mode**: Play with another human player.
- **Score Display**: Shows scores after each game.

### `cli.py`
Implements the Tic-Tac-Toe game using a command line interface.
- **Game Board**: Displayed in the console.
- **Player Moves**: Players enter their moves by typing the corresponding position number.
- **Single Player Mode**: Play against an AI.
- **Two Player Mode**: Play with another human player.
- **Score Tracking**: Scores are printed to the console after each game.

### `main.py`
The entry point for the project.
- **User Choice**: Prompts the user to choose between GUI and CLI versions.
- **Script Execution**: Runs the chosen script (`gui.py` or `cli.py`) using `subprocess`.

## How to Run the Project

1. **Ensure all scripts (`gui.py`, `cli.py`, `main.py`) are in the same directory.**
2. **Run the `main.py` script:**
    ```bash
    python main.py
    ```
3. **Follow the prompts to choose between the GUI or CLI version.**

## Conclusion

This project demonstrates the implementation of a classic game using two different interfaces, providing users with flexibility and an enjoyable experience. The use of algorithms like Minimax for the AI ensures challenging gameplay, while the Tkinter library provides a modern graphical user interface.
