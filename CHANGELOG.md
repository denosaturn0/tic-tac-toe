# Changelog

All notable changes to the Tic Tac Toe game will be documented in this file.

## [2.0.0] - 2026-02-08

### Added
- ✅ **Move Validation Feedback**: Players now receive clear confirmation when moves are valid
- ❌ **Detailed Error Messages**: Specific feedback for invalid moves:
  - Position already taken (shows which player occupies it)
  - Out of range positions (must be 1-9)
  - Invalid input types
- 📍 **Available Positions Display**: Shows remaining open positions before each turn
- 🎯 **Winning Combination Announcements**: Displays which combination won (e.g., "Top Row", "Middle Column", "Diagonal")
- 🎮 **Move Counter**: Tracks and displays total number of moves
- 📋 **Game Rules Display**: Shows comprehensive rules at game start
- 💡 **Helpful Tips**: Provides guidance to players throughout the game
- 🎉 **Enhanced Victory Messages**: Celebratory formatting for winners
- 🤝 **Tie Game Messages**: Special formatting for tie games
- ⚠️ **Graceful Interruption Handling**: Better messaging when game is interrupted
- 🔄 **New Game Indicator**: Clear messaging when restarting

### Enhanced
- Improved user experience with emoji indicators throughout
- Better visual separation between game phases
- More informative error handling
- Clearer player turn indicators

### Technical
- Added `winning_combo` attribute to track which combination won
- Enhanced `make_move()` method with detailed validation messages
- Updated `check_winner()` to identify and announce winning combinations
- Improved `play()` method with comprehensive game flow messages

## [1.0.0] - Initial Release

### Features
- Basic two-player Tic Tac Toe gameplay
- Win detection for rows, columns, and diagonals
- Tie game detection
- Position guide display
- Play again functionality
- Input validation
