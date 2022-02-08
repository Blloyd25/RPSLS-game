from player import Player
import random
class Computer(Player):
    
    def __init__(self):
        super().__init__()
        self.name = "Robot"

                # coming in from parent Player
        # self.list_of_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
        # self.wins = 0
        # self.choosen_gesture = "" 

    def choose_gesture(self):
        move = random.randrange(0,4)
        self.chosen_gesture = move
        print(f'Computer has selected  {self.gestures[move]}')
        pass