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
game_rules = "Rules: The first player to complete 3 of their marks in a row (up, down, across or diagonally) is the winner."
game_instructions = "Instructions: You must choose a spot on the board by entering a number ranging from 0 - 8 which match to the spots below. \n"
board_example = '0' + ' | ' + '1' + ' | ' + '2' + '\n' + '---------\n' + '3' + ' | ' + '4' + ' | ' + '5' + '\n' + '---------\n' + '6' + ' | ' + '7' + ' | ' + '8' + '\n'

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
            print('Available moves:', board.availableMoves()) # show player available moves

            while True:
                spot = int(input("X's turn, choose a spot (0 - 8): ")) # prompt player for spot on board
                print(board.player + " makes a move to square ", spot) # display players move choice

                # Check if spot is valid and set to proper row and column
                if spot >= 0 and spot <= 8:
                    row = spot // 3
                    column = spot % 3 
                
                    # check if spot is available
                    if [row, column] in board.availableMoves():
                        board.gameState[row][column] = 'X'
                        break
                    else:
                        print('That spot is not available. Try another spot.')
                
                # Player entered spot that is not valid        
                else:
                    print('That is not a valid spot. Try again.\n')

        # Computer turn code
        else:
            print("Computer's turn...") # display that it is computer's turn
            time.sleep(2) #sleep timer to simulate computer thinking

            available_moves = board.availableMoves() # set available moves to choose from
            computer_move = random.choice(available_moves) # set computer's move to random choice from available moves
            row, column = computer_move # assign row and column to computer move chosen

            spot = row * 3 + column
            print(board.player + " makes a move to square ", spot) # display players move choice

            board.gameState[row][column] = 'O' # set spot chosen to computer's value 'O'
            
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
