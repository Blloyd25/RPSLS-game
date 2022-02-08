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
            print('This game will be best of three good luck!')
        if user_input == 2:
            print('Good luck to you both and lets find us a champion!')

    def begin_round():

        pass

    def user_choice(playerone,playertwo,computer, user_move):
        user_move = {Playerone.chosen_gesture} or {Playertwo.chosen_gesture}

    def computer_player(self):
        self.move = random.choice(Computer.list_of_gestures)
        print('Computer has selected' + {Computer.choosen_gesture})
        

    def player_one_win(self, playertwo, computer,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            if self == opponent:
                print('It is a tie.') 
            return True
        else:
            return False

    def player_two_win(self, playerone,computer,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            if self == opponent:
                print('It is a tie.')
            return True
        else:
            return False

    def computer_win (self, playerone,playertwo,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            if self == opponent:
                print('It is a tie.')
            return True
        else:
            return False



    def is_win (playerone, playertwo, computer):
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

        if Self(playerone, playertwo, computer):
            return (1, playerone, playertwo, computer)

        return (-1, playerone, playertwo, computer)
