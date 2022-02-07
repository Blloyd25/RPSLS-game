class Gestures:
    move = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
    opponent = move

    def player_one_win(self, player_two, computer, move,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            return True
        else:
         return False

    def player_two_win(self, player_one,computer,move,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            return True
        else:
             return False

    def computer_win (self, player_one,player_two,move,opponent):
        if (self == 0 and opponent == 2, 3) or (self == 1 and opponent == 0,4) or (self == 2 and opponent == 1,3)or (self == 3 and opponent == 4,1) or (self == 4 and opponent == 2,0):
            return True
        else:
            return False



























    # 0        1           2         3         4
# ['rock', 'paper', 'scissors', 'lizard', 'spock' ]





















# Rock crushes Scissors   
# Scissors cuts Paper  
# Paper covers Rock  
# Rock crushes Lizard  
# Lizard poisons Spock  
# Spock smashes Scissors  
# Scissors decapitates Lizard  
# Lizard eats Paper  
# Paper disproves Spock  
# Spock vaporizes Rock 