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

# Main
if __name__ == '__main__':
    board = Board()
    board.printBoard()
    if board.player == 'X':
        print('Player goes first.')
    else:
        print('Computer goes first.')
    # while board.winner == None:
