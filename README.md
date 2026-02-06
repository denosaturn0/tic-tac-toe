# Tic Tac Toe Game

A simple command-line implementation of the classic Tic Tac Toe game written in Python.

## Features

- Clean command-line interface
- Two-player gameplay
- Input validation
- Win detection (rows, columns, diagonals)
- Tie game detection
- Play again option
- Position guide for easy reference

## Requirements

- Python 3.6 or higher

## Installation

1. Download or clone this repository
2. Navigate to the project directory

```bash
cd tic-tac-toe
```

## Usage

Run the game using Python:

```bash
python tic_tac_toe.py
```

Or make it executable (Linux/Mac):

```bash
chmod +x tic_tac_toe.py
./tic_tac_toe.py
```

## How to Play

1. The game displays a position guide showing numbers 1-9
2. Players take turns (X goes first)
3. Enter a number (1-9) to place your mark in that position
4. The first player to get three in a row (horizontally, vertically, or diagonally) wins
5. If all positions are filled with no winner, the game is a tie

### Position Guide

```
 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 
```

## Example Gameplay

```
Player X's turn
Enter position (1-9): 5

 X |   |   
---|---|---
   | X |   
---|---|---
   |   |   

Player O's turn
Enter position (1-9): 1
```

## Project Structure

```
tic-tac-toe/
├── tic_tac_toe.py    # Main game file
├── README.md          # This file
└── LICENSE            # MIT License
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements:

- Enhanced AI opponent
- GUI version
- Score tracking
- Different board sizes
- Network multiplayer

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Hassan

## Acknowledgments

- Classic Tic Tac Toe game rules
- Python community for best practices
