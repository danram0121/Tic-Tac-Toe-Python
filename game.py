# Imports
import math
import random
import time # for sleep

# Definitions
class Board():
    def __init__(self):
        self.gameState = self.setGameState()
        self.player = self.coinToss()
        self.winner = None        
    # Methods
    def coinToss(self):
        return 'X' if random.choice([0, 1]) == 0 else 'O'
    
    def setGameState(self):
        return [[' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']]
    
    def availableMoves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.gameState[i][j] == ' ':
                    moves.append([i, j])
        return moves
    
    def printBoard(self):
        return print(self.gameState[0][0] + ' | ' + self.gameState[0][1] + ' | ' + self.gameState[0][2] + '\n' +
                     '---------\n' +
                     self.gameState[1][0] + ' | ' + self.gameState[1][1] + ' | ' + self.gameState[1][2] + '\n' +
                     '---------\n' +
                     self.gameState[2][0] + ' | ' + self.gameState[2][1] + ' | ' + self.gameState[2][2] + '\n')
    
    def checkTie(self):
    # check if any spaces are left empty OR if theres a winner, if neither, return True
        for i in range(3):
            for j in range(3):
                if self.gameState[i][j] == ' ' and self.winner == None:
                    return False
        return True

    def CheckWin(self):
        # Check rows
        for i in range(3):
            if self.gameState[i][0] == self.gameState[i][1] == self.gameState[i][2] != ' ':
                return True
        # Check columns
        for i in range(3):
            if self.gameState[0][i] == self.gameState[1][i] == self.gameState[2][i] != ' ':
                return True
        # Check diagonals
        if self.gameState[0][0] == self.gameState[1][1] == self.gameState[2][2] != ' ':
            return True
        if self.gameState[0][2] == self.gameState[1][1] == self.gameState[2][0] != ' ':
            return True
        return False

intro_message = "* * * * * * * * * * * * * Welcome to Tic-Tac-Toe * * * * * * * * * * * * *"
game_rules = "Rules: The first player to complete 3 of their marks in a row (up, down, across or diagonally) is the winner"
game_instructions = "Instructions: The player chooses their spot by choosing (column, row) which range from 0 - 2 i.e. choosing  1 2  creates the following board"
board_example = ' ' + ' | ' + ' ' + ' | ' + ' ' + '\n' + '---------\n' + ' ' + ' | ' + ' ' + ' | ' + 'X' + '\n' + '---------\n' + ' ' + ' | ' + ' ' + ' | ' + ' ' + '\n'

# Main
if __name__ == '__main__':
    print('\n' + intro_message)
    print(game_rules)
    print(game_instructions)
    print(board_example + '\n')

    # start game, maybe while loop here to check whether player wants to play again
    print('Game Start\n')
    board = Board() # initialize board
    board.printBoard() # show empty board to player
    
    # print starting player
    if board.player == 'X':
        print('Player goes first.')
    else:
        print('Computer goes first.')
    
    # Game Loop
    while board.winner == None:
        # Player turn
        if board.player == 'X': 
            testPlayer = input('inside player turn: \n')
            print('Available moves:', board.availableMoves()) # show player available moves

        # Computer turn code
        else:
            testComp = input('inside comp turn: \n')

        # Print new board state
        board.printBoard()

        # Check for win
        if board.CheckWin():
            # board.winner == board.player
            test_win = input('inside CheckWin condition: \n')
            print(board.player + " has won! \n")          
            # Set ask user to play again or quit

        # Check for tie
        elif board.checkTie():
            test_win = input('inside checkTie condition: \n')
            print('The game has ended in a draw.')
            # Set ask user to play again or quit
        
        # Switch player for next turn
        if board.player == 'X':
            board.player = 'O'
        else:
            board.player = 'X'
