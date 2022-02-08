from computer import Computer
from human import Human

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
   
    welcome = print(' Welcome to RPSLS its a very nerdy game ')
    rules = print('The rules are as follows: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock ')
   
    def confirm_play(self,user_input):
        user_input = input('Please select how many players will be playing in todays game')
        if user_input =="1":
            self.player_two = Computer()
            print('good luck' + {self.player_one.name} + 'dont underestimate this computer!')
        if user_input =="2":
            self.player_two = Human()
            print('Good luck' + {self.player_one.name} + 'and' + {self.player_two.name} + 'to you both and lets find us a champion!')
       
    
    def play(self):
        self.confirm_play()
        self.play_round()
       
       
       
       
        # if result == 0:
        #         print('Its a tie')

        # if result ==1: 
        #         playertwo_wins += 1
        #         print('player 2 wins!') 

        # if result == 1:
        #         playerone_wins += 1
        #         print('You won GG!')
        # if result == 1:
        #         computer_wins += 1
        #         print('Computer wins')

    def play_round(self):
        print("starting a round of RPSLS")
        self.player_one.choose_gesture()  # this saves the gesture choice to self.player_one.chosen_gesture
        self.player_two.choose_gesture()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("it is a tie, play again")
        elif (self.player_one.chosen_gesture == 0) and (self.player_two.chosen_gesture == 2 or self.player_two.chosen_gesture == 3):
            print("player one wins this round ")
            self.player_one.wins += 1
        elif (self.player_one.chosen_gesture == 0) and (self.player_two.chosen_gesture == 2 or self.player_two.chosen_gesture == 3):
            print("player one wins this round ")
            self.player_one.wins += 1
        else:
            print("player 2 wins this hand")
            print(f'{self.player_two.name} won the round with {self.player_two.chosen_gesture} ')
            self.player_two.wins += 1
        
        
         or (self == 1 and playerone == 0,4) or
         
          (self == 2 and playerone == 1,3)or 
          
          (self == 3 and playerone == 4,1) or 
          
          (self == 4 and playerone == 2,0):
            if self == playerone:
                print('Its a tie.')
          
    def play_best_of(playerone_wins,playertwo_wins, computer_wins):


            while playerone_wins < wins_needed and computer_wins < wins_needed and playertwo_wins < wins_needed:

                playerone_wins = 0
                playertwo_wins = 0
                computer_wins = 0
                wins_needed = 3
                playerone_wins, playertwo_wins, computer_wins = self.play()

            if playerone_wins > wins_needed:
                print('You have won the best of 3 games!')

            if playertwo_wins > wins_needed:
                print('You have won the best of 3 games!')

            if computer_wins >  wins_needed:  
                print('You have won the best of 3 games!')


            elif playerone_wins == computer_wins:
                return (0, playerone_wins, playertwo_wins, computer_wins)

            elif playerone_wins == playertwo_wins:
                return (0, playerone_wins, playertwo_wins, computer_wins)

            elif playerone_wins or playertwo_wins or computer_wins:
                return (1, playerone_wins, playertwo_wins, computer_wins)
            return (-1, playerone_wins, playertwo_wins, computer_wins)
            
