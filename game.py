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
        self.mode = None       
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



    #  I think calling playAgain() here is causing the game to run multiple modes at once
    def CheckWin(self):
        # Check for tie first
        if board.checkTie():
            print('The game has ended in a draw.')
            board.playAgain()
        # Check for win now
        # Check rows
        for i in range(3):
            if self.gameState[i][0] == self.gameState[i][1] == self.gameState[i][2] != ' ':
                print("Player " + self.gameState[i][0] + " has won!")
                board.winner = self.gameState[i][0] # set winner to player
                board.playAgain()
        # Check columns
        for i in range(3):
            if self.gameState[0][i] == self.gameState[1][i] == self.gameState[2][i] != ' ':
                print("Player " + self.gameState[0][i] + " has won!")
                board.winner = self.gameState[0][i] # set winner to player  
                board.playAgain()
        # Check diagonals
        if self.gameState[0][0] == self.gameState[1][1] == self.gameState[2][2] != ' ':
            print("Player " + self.gameState[0][0] + " has won!")
            board.winner = self.gameState[0][0] # set winner to player
            board.playAgain()
        if self.gameState[0][2] == self.gameState[1][1] == self.gameState[2][0] != ' ':
            print("Player " + self.gameState[0][2] + " has won!")
            board.winner = self.gameState[0][2] # set winner to player
            board.playAgain()
        # If no winner, return False here to continue game
    


    def playAgain(self):
        # Ask player if they want to play again
        while True:
            user_input = input('\nWould you like to play again? (y/n): ').lower()
            if user_input == 'y':
                # Create a new instance of the Board class
                global board  # reference the global variable
                board = Board()
                print("\nStarting a new game.\n")
                board.game()  
                break
            elif user_input == 'n':
                print('\nThanks for playing!')
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")




    def playerMove(self, movesList):
        print('Available moves:', board.availableMoves()) # show player available moves

        while True:
            try:
                spot = int(input(board.player + "'s turn, choose a spot (0 - 8): ")) # prompt player for spot on board
                
                # Check if spot is valid and set to proper row and column
                if spot >= 0 and spot <= 8:
                    print(board.player + " makes a move to square ", spot) # display player's move choice
                    row = spot // 3
                    column = spot % 3 

                    # check if spot is available
                    if [row, column] in board.availableMoves():
                        board.gameState[row][column] = board.player # set spot chosen to player's value 
                        break
                    else:
                        print('That spot is not available. Try another spot.')
                else:
                    print('That is not a valid spot. Try again.\n')

            except ValueError:
                print('Invalid input. Please enter a valid integer.')


    # Random Move Computer Player
    def randomMove(self, movesList):
        print("Computer's turn...") # display that it is computer's turn
        time.sleep(2) #sleep timer to simulate computer thinking

        available_moves = board.availableMoves() # set available moves to choose from
        computer_move = random.choice(available_moves) # set computer's move to random choice from available moves
        row, column = computer_move # assign row and column to computer move chosen

        spot = row * 3 + column
        print(board.player + " makes a move to square ", spot) # display players move choice

        board.gameState[row][column] = 'O' # set spot chosen to computer's value 'O'


    # Minmax / Adverserial Computer Player
    def minMax(self, movesList):
        pass
    
    def pickMode(self):
        print("Choose an opponent to play against:\n")
        print("\t1. Player vs. Player")
        print("\t2. Player vs. Random Choice")
        print("\t3. Player vs. MinMax AI\n")
        
        # Prompt player for mode choice
        while True:
            try:
                mode = int(input("Choose a mode (1 - 3): "))
                if mode == 1:
                    board.mode = 'PvP'
                    print('\nYou have chosen Player vs. Player mode.\n')
                    break
                elif mode == 2:
                    board.mode = 'PvR'
                    print('\nYou have chosen Player vs. Random Choice mode.\n')
                    break
                elif mode == 3:
                    board.mode = 'PvM'
                    print('\nYou have chosen Player vs. MinMax AI mode.\n')
                    break
                else:
                    print('That is not a valid mode. Try again.\n')
            except ValueError:
                print('Invalid input. Please enter a valid integer.\n')
    
    # Game Mode for Player vs Player
    def pvp(self):
        # print starting player
        if board.player == 'X':
            print('Player X goes first.\n')
        else:
            print('Player O goes first.\n')

        while board.winner == None:
            # Player turn
            if board.player == 'X': 
                board.playerMove(board.availableMoves())

            # Computer turn code
            else:
                board.playerMove(board.availableMoves())
                
            # Print new board state
            board.printBoard()

            # Check for win or tie
            board.CheckWin()
            
            # Switch player for next turn
            if board.player == 'X':
                board.player = 'O'
            else:
                board.player = 'X'

    # Game Mode for Player vs Random Choice
    def pvr(self):
        while board.winner == None:
            # Player turn
            if board.player == 'X': 
                board.playerMove(board.availableMoves())

            # Computer turn code
            else:
                board.randomMove(board.availableMoves())
                
            # Print new board state
            board.printBoard()

            # Check for win or tie
            board.CheckWin()
            
            # Switch player for next turn
            if board.player == 'X':
                board.player = 'O'
            else:
                board.player = 'X'

    # Game Mode for Player vs MinMax AI
    def pvm(self):
        print("AI mode not yet implemented")
        
    
    def info(self):
        # Print intro message, rules, instructions
        intro_message = "* * * * * * * * * * * * * Tic-Tac-Toe * * * * * * * * * * * * *"
        game_rules = "Rules: The first player to complete 3 of their marks in a row (up, down, across or diagonally) is the winner."
        game_instructions = "Instructions: You must choose a spot on the board by entering a number ranging from 0 - 8 which match to the spots below. \n"
        
        # Print intro message, rules, instructions
        print('\n' + intro_message)
        print(game_rules)
        print(game_instructions)
    
    def game(self):    
        # prompt player for mode choice
        board.pickMode() 
        # print board example
        board_example = '0' + ' | ' + '1' + ' | ' + '2' + '\n' + '---------\n' + '3' + ' | ' + '4' + ' | ' + '5' + '\n' + '---------\n' + '6' + ' | ' + '7' + ' | ' + '8' + '\n'
        print(board_example + '\n')
        # print empty board
        board.printBoard() 
        # Check Game Mode Here (PvP, PvR, PvM)
        if board.mode == 'PvP':
            board.pvp()
        elif board.mode == 'PvR':
            board.pvr()
        elif board.mode == 'PvM':
            board.pvm()
        else:
            print('Something went wrong. Game mode needs to be set. Exiting game.')
            exit()
        
       


# Main
if __name__ == '__main__':
    

    # start game, maybe while loop here to check whether player wants to play again
    print('Game Start\n')
    board = Board() # initialize board
    board.game() # start game
    
