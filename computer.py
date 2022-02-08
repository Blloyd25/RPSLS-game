from pickle import LIST
import random
class Computer:
    
    def computer_ai(self, list_of_gestures):

        self.list_of_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
        self.wins = 0
        self.choosen_gesture = random.choice(list_of_gestures)

   