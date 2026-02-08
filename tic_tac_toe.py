#!/usr/bin/env python3
"""
Tic Tac Toe Game
A simple command-line implementation of the classic Tic Tac Toe game.
"""

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.winning_combo = None
        self.game_over = False
        
    def display_board(self):
        """Display the current state of the board."""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")
        
    def display_position_guide(self):
        """Display the position numbering guide."""
        print("\nPosition Guide:")
        print(" 1 | 2 | 3 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 7 | 8 | 9 ")
        print()
        
    def make_move(self, position):
        """
        Make a move at the specified position.
        
        Args:
            position (int): Position on the board (1-9)
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        if position < 1 or position > 9:
            print("❌ Invalid position! Please choose a number between 1 and 9.")
            return False
            
        index = position - 1
        if self.board[index] != ' ':
            print(f"❌ Position {position} is already taken by '{self.board[index]}'! Choose another position.")
            return False
            
        self.board[index] = self.current_player
        print(f"✅ Valid move! Player {self.current_player} placed at position {position}")
        return True
        
    def check_winner(self):
        """Check if there's a winner or a tie."""
        # Winning combinations
        winning_combinations = [
            ([0, 1, 2], "Top Row"),
            ([3, 4, 5], "Middle Row"),
            ([6, 7, 8], "Bottom Row"),
            ([0, 3, 6], "Left Column"),
            ([1, 4, 7], "Middle Column"),
            ([2, 5, 8], "Right Column"),
            ([0, 4, 8], "Diagonal (Top-Left to Bottom-Right)"),
            ([2, 4, 6], "Diagonal (Top-Right to Bottom-Left)")
        ]
        
        for combo, description in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                self.winner = self.board[combo[0]]
                self.winning_combo = description
                self.game_over = True
                print(f"\n🎯 Winning combination: {description}!")
                return True
                
        # Check for tie
        if ' ' not in self.board:
            self.game_over = True
            return True
            
        return False
        
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
    def play(self):
        """Main game loop."""
        print("=" * 40)
        print("  Welcome to Tic Tac Toe!")
        print("=" * 40)
        print("\n📋 Game Rules:")
        print("   • Two players take turns (X and O)")
        print("   • First to get 3 in a row wins!")
        print("   • Rows, columns, or diagonals count")
        print("   • If all 9 spaces fill up, it's a tie")
        self.display_position_guide()
        print("💡 Tip: Use the position numbers (1-9) to make your move\n")
        
        move_count = 0
        
        while not self.game_over:
            self.display_board()
            move_count += 1
            print(f"🎮 Move #{move_count} - Player {self.current_player}'s turn")
            
            # Show available positions
            available = [str(i+1) for i, spot in enumerate(self.board) if spot == ' ']
            print(f"📍 Available positions: {', '.join(available)}")
            
            try:
                position = int(input("Enter position (1-9): "))
                
                if self.make_move(position):
                    if self.check_winner():
                        self.display_board()
                        if self.winner:
                            print("🎉" * 15)
                            print(f"   🏆 PLAYER {self.winner} WINS! 🏆")
                            print("🎉" * 15)
                            print(f"\n✨ Game completed in {move_count} moves!")
                        else:
                            print("🤝" * 15)
                            print("     IT'S A TIE GAME!")
                            print("🤝" * 15)
                            print(f"\n✨ All 9 positions filled - Well played!")
                        break
                    self.switch_player()
                    
            except ValueError:
                print("❌ Invalid input! Please enter a number between 1 and 9.")
            except KeyboardInterrupt:
                print("\n\n⚠️  Game interrupted. Thanks for playing!")
                break
                
        # Ask to play again
        print("\n" + "─" * 40)
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'y':
            print("\n🔄 Starting new game...\n")
            self.__init__()
            self.play()
        else:
            print("\n👋 Thanks for playing! Goodbye!")


def main():
    """Entry point for the game."""
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()
