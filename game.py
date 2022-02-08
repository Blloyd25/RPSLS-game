import random
from computer import Computer
from playerone import Playerone
from playertwo import Playertwo
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


    def user_choice(playerone,playertwo,computer):
        print({Playerone.chosen_gesture}) or ({Playertwo.chosen_gesture})

    def computer_player(self):
        self.move = random.choice(Computer.list_of_gestures)
        print('Computer has selected' + {Computer.choosen_gesture})
          
    def begin_round():

        pass

    def is_win (playerone, playertwo, computer,self):
        if playerone > computer:
            print('You have won the best of 3 games!')
        if playertwo > computer:
            print('You have won the best of 3 games!')
        if playerone > playertwo:  
            print('You have won the best of 3 games!')
        if playertwo > playerone:
            print('You have won the best of 3 games!')


        if playerone == computer:
            return (0, playerone, playertwo, computer)
        if playerone == playertwo:
            return (0, playerone, playertwo, computer)

        if self(playerone, playertwo, computer):
            return (1, playerone, playertwo, computer)

        return (-1, playerone, playertwo, computer)
pass