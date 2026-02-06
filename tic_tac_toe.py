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
            print("Invalid position! Please choose a number between 1 and 9.")
            return False
            
        index = position - 1
        if self.board[index] != ' ':
            print("That position is already taken! Choose another.")
            return False
            
        self.board[index] = self.current_player
        return True
        
    def check_winner(self):
        """Check if there's a winner or a tie."""
        # Winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                self.winner = self.board[combo[0]]
                self.game_over = True
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
        self.display_position_guide()
        
        while not self.game_over:
            self.display_board()
            print(f"Player {self.current_player}'s turn")
            
            try:
                position = int(input("Enter position (1-9): "))
                
                if self.make_move(position):
                    if self.check_winner():
                        self.display_board()
                        if self.winner:
                            print(f"🎉 Player {self.winner} wins! 🎉")
                        else:
                            print("It's a tie!")
                        break
                    self.switch_player()
                    
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Goodbye!")
                break
                
        # Ask to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y':
            self.__init__()
            self.play()


def main():
    """Entry point for the game."""
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()
