# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class GameBoard:
    """making and printing the game board
    """
    def __init__(self, board):
        self.board = board
        
    def print_board(self):
        # visualise the board 
        print("  1 2 3 4 5")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """ 
    making the battleship class to craet and guess the ships location
    """
    
    def __init__(self, board):
        self.board = board
    
    def create_ships(self):
        # creat five random ships for both the user and the computer
        for ship in range(5):
            self.row = random.randint(0, 4)
            self.column = random.randint(0, 4)
            while self.board[self.row][self.column] == "X":
                self.row = random.randint(0, 4)
                self.column = random.randint(0, 4)
            self.board[self.row][self.column] = "X"
        return self.board


# create to type of board for each gamer : the guess board
# and the one with the ships place on it                 
computer_board = GameBoard([[" "] * 5 for i in range(5)])
player_guess_board = GameBoard([[" "] * 5 for i in range(5)])
player_board = GameBoard([[" "] * 5 for i in range(5)])
computer_guess_board = GameBoard([[" "] * 5 for i in range(5)])
Battleship.create_ships(computer_board)
Battleship.create_ships(player_board)
print("where the computer's battleships are hidden")
GameBoard.print_board(player_board)
print("your guess board")
GameBoard.print_board(player_guess_board)


# GameBoard.print_board((computer_board))
