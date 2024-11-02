'''Info'''
# Name: Venkata Siva Reddy Naga
# UFID: 97561398
# Major: Applied Data Science

"""
Description: This Tic Tac Toe game is played on a 3x3 grid by two players who take turns placing their marks, X and O, in the available spaces.
The game is designed to start a new round, ask players for their moves, update the game board, handle incorrect inputs, and check for winners.
This code uses classes and objects.
"""

# Class for the game board
class Board:
    def __init__(self):
        # Create a 3x3 board filled with empty spaces
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def printBoard(self):
        # Display the board with row and column labels
        board_form = ["|R\\C| 0 | 1 | 2 |"]
        for i in range(3):
            board_form.append(f"| {i} | {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} |")
        for row in board_form:
            print("------------------")
            print(row)
        print("------------------")

    def updateBoard(self, row, col, player):
        # Put the player's mark on the board if the cell is empty
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False


# Class to manage the game
class Game:
    def __init__(self):
        # Set up the board and start with player 'X'
        self.board = Board()
        self.turn = 'X'
        self.selection_count = 0  # Track number of moves

    def switchPlayer(self):
        # Change the turn between 'X' and 'O'
        self.turn = 'O' if self.turn == 'X' else 'X'

    def validateEntry(self, row, col):
        # Check if the move is within the board and the cell is empty
        if 0 <= row < 3 and 0 <= col < 3 and self.board.board[row][col] == " ":
            return True
        # If the move is out of bounds or the cell is taken, print an error message
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid entry: try again. Row & column numbers must be 0, 1, or 2.")
        elif self.board.board[row][col] != " ":
            print("That cell is already taken. Please make another selection.")
        return False

    def checkWin(self):
        # Check rows, columns, and diagonals for a win
        b = self.board.board
        for i in range(3):
            # Check if all cells in a row or column match the player's mark
            if all(b[i][j] == self.turn for j in range(3)) or all(b[j][i] == self.turn for j in range(3)):
                return True
        # Check both diagonals
        if b[0][0] == b[1][1] == b[2][2] == self.turn or b[0][2] == b[1][1] == b[2][0] == self.turn:
            return True
        return False

    def checkFull(self):
        # Check if all cells are filled
        return self.selection_count == 9

    def checkEnd(self):
        # Check if the game is over
        if self.checkWin():
            # If a player wins, show a message and the board
            print(f"{self.turn} IS THE WINNER!!!")
            self.board.printBoard()
            return True
        if self.checkFull():
            # If no cells are empty, it’s a draw
            print("DRAW! NOBODY WINS!")
            self.board.printBoard()
            return True
        return False

    def playGame(self):
        # Main game loop
        print("New Game: X goes first.")
        self.board.printBoard()

        while True:
            print(f"\n{self.turn}'s turn.")
            position = input(f"Where do you want your {self.turn} placed? Enter row and column separated by a comma:\n")

            try:
                # Convert user input into row and column
                row, col = map(int, position.split(","))
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")
                continue

            if self.validateEntry(row, col):
                # If the move is valid, update the board and show it
                if self.board.updateBoard(row, col, self.turn):
                    self.selection_count += 1
                    self.board.printBoard()

                    # Check if the game is over
                    if self.checkEnd():
                        break

                    # Switch to the other player
                    self.switchPlayer()
                else:
                    print("Invalid move! Try again.")
            else:
                continue

        # Ask if players want another game
        another_game = input("\nAnother game? Enter Y or y for yes.\n")
        if another_game.lower() == 'y':
            # Restart the game if yes
            self.__init__()
            self.playGame()
        else:
            print("Thank you for playing!")


# Start the game if this file is run directly
if __name__ == "__main__":
    game = Game()
    game.playGame()
