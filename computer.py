from playerone import Playerone
import random
from playerone import Playerone
class Computer:
    
    def computer_ai(self, list_of_gestures):

        self.list_of_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
        self.wins = 0
        self.choosen_gesture = random.choice(list_of_gestures)

    def computer_win (self, playerone):
        if (self == 0 and playerone == 2, 3) or (self == 1 and playerone == 0,4) or (self == 2 and playerone == 1,3)or (self == 3 and playerone == 4,1) or (self == 4 and playerone == 2,0):
            if self == playerone:
                print('Its a tie.')
            return True
        else:
            return False