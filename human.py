from player import Player
class Human(Player):
   
   def __init__(self):
       super().__init__()
       self.set_name()

       # these will be added by the parent class
    # self.list_of_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
    # self.wins = 0
    # set name 
    

def player_two_win(self, playerone):
        if (self == 0 and playerone == 2, 3) or (self == 1 and playerone == 0,4) or (self == 2 and playerone == 1,3)or (self == 3 and playerone == 4,1) or (self == 4 and playerone == 2,0):
            if self == playerone:
                print('It is a tie.')
            return True
        else:
            return False

def choose_gesture(self):
    count = 0
    for gesture in self.gestures:
        print(f'Press {count} to select {gesture}')
        count += 1
    self.choosen_gesture = int(input('Please select your move'))
    pass

def set_name(self):
    user_input = input("enter you name")
    self.name = user_input