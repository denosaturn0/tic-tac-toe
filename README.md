# Tic Tac Toe Game

A simple command-line implementation of the classic Tic Tac Toe game written in Python.

## Features

- Clean command-line interface with emoji indicators
- Two-player gameplay
- **Enhanced move validation with detailed feedback**
- **Real-time move confirmation messages**
- **Available positions display**
- **Move counter and game statistics**
- **Winning combination announcement** (e.g., "Top Row", "Diagonal")
- Win detection (rows, columns, diagonals)
- Tie game detection
- Play again option
- Position guide for easy reference
- **Comprehensive game rules displayed at start**
- **Error messages for invalid inputs**

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
========================================
  Welcome to Tic Tac Toe!
========================================

📋 Game Rules:
   • Two players take turns (X and O)
   • First to get 3 in a row wins!
   • Rows, columns, or diagonals count
   • If all 9 spaces fill up, it's a tie

Position Guide:
 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 

💡 Tip: Use the position numbers (1-9) to make your move


   |   |   
---|---|---
   |   |   
---|---|---
   |   |   

🎮 Move #1 - Player X's turn
📍 Available positions: 1, 2, 3, 4, 5, 6, 7, 8, 9
Enter position (1-9): 5
✅ Valid move! Player X placed at position 5


   |   |   
---|---|---
   | X |   
---|---|---
   |   |   

🎮 Move #2 - Player O's turn
📍 Available positions: 1, 2, 3, 4, 6, 7, 8, 9
Enter position (1-9): 1
✅ Valid move! Player O placed at position 1

[Game continues...]

🎯 Winning combination: Diagonal (Top-Left to Bottom-Right)!
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
   🏆 PLAYER X WINS! 🏆
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉

✨ Game completed in 9 moves!
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
