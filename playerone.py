from unicodedata import name


class Playerone:

    def player_one(self, list_of_gestures):

        self.list_of_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
        self.wins = 0
        self.name =  input('Please enter your name')
        self.choosen_gesture = input('Please select your move' + {list_of_gestures})