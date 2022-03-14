import os
import random
import sys
# Manage errors

class rock_paper_scissor():

    def __init__(self):
        # Initializing Game
        print("-------- Welcome To Rock, Paper and Scissors --------\n")
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.all_moves = {'r' : 'Rocks', 'p' : 'Paper', 's' : 'Scissors'}
        self.combinations = {'r' : 'p', 'p' : 's', 's' : 'r'}


    def main_game(self):

        while True:
            os.system('cls')
            print(f"{self.wins} wins, {self.losses} losses, {self.ties} ties\n")
        
            # Player Move
            self.player_move = input("Choose a move. (r)ock, (p)paper or (s)cissor. 'q' to exit: ")
            # In case of exit
            if self.player_move == 'q':
                sys.exit()

            # Printing the user move
            print(f"\nPlaying {self.all_moves[self.player_move]}...")

            # Computer Random Move
            print("\nGenerating Computer Move...")
            self.cpu_move = random.choice(list(self.all_moves))
            print(f'Computer plays {self.all_moves[self.cpu_move]}!')
            
            # In case of tie
            if self.player_move == self.cpu_move:
                print("\nIt's a Tie!!!")
                self.ties += 1

            # In case of win
            elif self.combinations[self.player_move] != self.cpu_move:
                print("\nYou're the WINNER!!!")
                self.wins += 1

            # In case of lose
            elif self.combinations[self.player_move] == self.cpu_move:
                print("\nComputer wins!!!")
                self.losses += 1

            


if __name__ == '__main__':
    game = rock_paper_scissor()
    game.main_game()
    
