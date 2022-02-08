
from computer import Computer
from playertwo import Playertwo
from computer import Computer
from playertwo import Playertwo
class Playerone:

    def player_one(self, list_of_gestures):

        self.list_of_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
        self.wins = 0
        self.name =  input('Please enter your name')
        self.choosen_gesture = input('Please select your move' + {list_of_gestures})

    def player_one_win(self, playertwo, computer,opponent):
        opponent = playertwo or computer
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            if self == opponent:
                print('It is a tie.') 
            return True
        else:
            return False  