import random
from computer import Computer
from playerone import Playerone
from playertwo import Playertwo

def rules_of_game():

    greeting = input(' Welcome to RPSLS its a very nerdy game ')
    rules = input('The rules are as follows: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock ')
    


def confirm_play(user_input):
    user_input = input('Please select how many players will be playing in todays game')
    if user_input == 1:
        print('This game will be best of three good luck!')
    if user_input == 2:
        print('Good luck to you both and lets find us a champion!')

def begin_round():

    pass

def user_choice(player_one,player_two,computer):
    pass

def computer_player(self):
    self.move = random.choice(Computer.list_of_gestures)
    pass

def player_one_win(self, player_two, computer,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            if self == opponent:
                print('It is a tie.') 
            return True
        else:
            return False

def player_two_win(self, player_one,computer,move,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            if self == opponent:
                print('It is a tie.')
            return True
        else:
            return False

def computer_win (self, player_one,player_two,move,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            if self == opponent:
                print('It is a tie.')
            return True
        else:
            return False



def is_win (playerone, playertwo, computer):
    if playerone or playertwo > computer:
        print('You have won the best of 3 games! What a champ')
    else:
        print('Unfortunately, the computer has won the best of 3 games. Better luck next time!')

    if playerone or playertwo == computer:
        return (0, playerone, playertwo, computer)
   
    if is_win(playerone, playertwo, computer):
        return (1, playerone, playertwo, computer)

    return (-1, playerone, playertwo, computer)
pass