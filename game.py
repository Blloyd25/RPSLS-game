import random
from computer import Computer
from playerone import Playerone
from playertwo import Playertwo, player_two_win
import math
class Game:

    def rules_of_game(self):

        self.welcome =input(' Welcome to RPSLS its a very nerdy game ')
        self.rules = input('The rules are as follows: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock ')
   
    def confirm_play(user_input):
        user_input = input('Please select how many players will be playing in todays game')
        if user_input == 1:
            print('good luck') + {Playerone.__name__} + ('dont underestimate this computer!')
        if user_input == 2:
            print('Good luck') + {Playerone.__name__} + 'and' + {Playertwo.__name__}('to you both and lets find us a champion!')



    def user_choice(playerone,playertwo):
        print({playerone.chosen_gesture}) or ({playertwo.chosen_gesture})

    def computer_player(self):
        self.move = random.choice(Computer.list_of_gestures)
        print('Computer has selected' + {Computer.choosen_gesture})
    
    def play():

          
        def play_best_of(playerone_wins,playertwo_wins, computer_wins):


            while playerone_wins < wins_needed and computer_wins < wins_needed and playertwo_wins < wins_needed:

                playerone_wins = 0
                playertwo_wins = 0
                computer_wins = 0
                wins_needed = 3
                result, playerone_wins, playertwo_wins, computer_wins = play()

            if result == 0:
                print('Its a tie')

            if result ==1: 
                playertwo_wins += 1
                print('player 2 wins!') 

            if result == 1:
                playerone_wins += 1
                print('You won GG!')
            if result == 1:
                computer_wins += 1
                print('Computer wins')

            if playerone_wins > wins_needed:
                print('You have won the best of 3 games!')

            if playertwo_wins > wins_needed:
                print('You have won the best of 3 games!')

            if computer_wins >  wins_needed:  
                print('You have won the best of 3 games!')


            elif playerone_wins == computer_wins:
                return (0, playerone_wins, playertwo_wins, computer_wins)

            elif playerone_wins == playertwo_wins:
                return (0, playerone_wins, playertwo_wins, computer_wins)

            elif playerone_wins or playertwo_wins or computer_wins:
                return (1, playerone_wins, playertwo_wins, computer_wins)
            return (-1, playerone_wins, playertwo_wins, computer_wins)
