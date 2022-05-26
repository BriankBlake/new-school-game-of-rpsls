from ai import Ai 
from human import Human
import time,random,sys

from player import Player

class Game():
    def __init__(self):
        self.human = Human()
        self.ai = Ai()
      
    def run_game(self):
        self.display_welcome()
        self.game_choice()
        self.display_winner()
        self.restart()
       

    def display_welcome(self):
        print('Welcome to the best classic game ever of (R)ock, (P)aper, (S)cissors, (L)izard, (Sp)ock')
        time.sleep(2)    
        print('The game will be played as best two out of three games!')
        time.sleep(2)
        print('R destroys S!')
        time.sleep(1.5)
        print('S cuts P!')
        time.sleep(1.5)
        print ('P covers R!')
        time.sleep(1.5)
        print('R kills L!') 
        time.sleep(1.5)
        print('L poisons S!')
        time.sleep(1.5)
        print('Sp destroys S!')
        time.sleep(1.5)
        print('S kills L!')
        time.sleep(1.5)
        print('L eats P!')
        time.sleep(1.5)
        print('Sp burns P!')
        time.sleep(1.5)
        print('Sp smashes R!')
        time.sleep(1.5)
        print('R kills Sp!')  
        time.sleep(1.5)

        # Count to three with dramatic pauses:
        time.sleep(2)
        print('1...')
        time.sleep(2)
        print('2...')
        time.sleep(2)
        print('3...')
        time.sleep(2)
        print('Let get ready to rumble!')

    def game_choice(self):
        while True:
            try:    
                game_type = int(input('Which game would you like to play? For PvP, Press (1), for PvA, Press (2): '))
            except ValueError:
                print('not a valid selection please try again')
                continue

            if game_type == 2:
                print('You selected PvA.')
                self.computer_game()
                break
            elif game_type == 1:
                print('You selected PvP.')
                self.human_game()
                break
            else:  
                print('Sorry, only P or A') 
        

    def human_game(self):
        
        self.player01 = Human() 
        player_01 = self.player01.create_players()
        
        self.player02 = Human()
        player_02 = self.player02.create_players()
        self.player01.name = player_01
        self.player02.name = player_02
        print(f'(0)  {self.player01.gestures[0]}   (1) {self.player01.gestures[1]}  (2) {self.player01.gestures[2]} (3)  {self.player01.gestures[3]}     (4) {self.player01.gestures[4]} ')
        while self.player02.score != 2 and self.player01.score != 2:
            comp_player1 = self.human.choose_gesture()
            comp_player2 = self.human.choose_gesture()
            self.compare_gestures(comp_player1, comp_player2)
            
    def computer_game(self):
        
        self.player01 = Human() 
        player_01 = self.player01.create_players()
        
        
        self.player02 = Ai()
        self.player01.name = player_01
        print(f'(0)  {self.player01.gestures[0]}   (1) {self.player01.gestures[1]}  (2) {self.player01.gestures[2]} (3)  {self.player01.gestures[3]}     (4) {self.player01.gestures[4]} ')
        while self.player02.score != 2 and self.player01.score != 2:
            comp_player = self.human.choose_gesture()
            comp_random = self.ai.ai_gesture()
            self.compare_gestures(comp_player, comp_random)
            print(self.player01.score)
            print(self.player02.score)
    

    def compare_gestures(self,gesture_01,gesture_02):
        gesture_a = self.player01.gestures[gesture_01]
        gesture_b = self.player02.gestures[gesture_02]
        print(f'{self.player01.name} chooses {gesture_a}')
        time.sleep(2)
        print(f'{self.player02.name} chooses {gesture_b}')
        time.sleep(2)
        
        if gesture_b == gesture_a:
            print('It\'s a tie! Please try again!\n')
            self.player01.score += 0       
            
        elif 'R' in gesture_a:
            if 'P' in gesture_b: 
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(1.5)
                self.player02.score +=1
            elif 'Sp' in gesture_b:
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(1.5)
                self.player02.score +=1
            
            else:
                print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                time.sleep(1.5)
                self.player01.score +=1

        elif 'P' in gesture_a:
            if 'L' in gesture_b: 
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(1.5)
                self.player02.score +=1

            elif 'S' in gesture_b:
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(1.5)
                self.player02.score +=1

            else:
                print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                time.sleep(1.5)
                self.player01.score +=1

        elif 'S' in gesture_a:
            if 'R' in gesture_b: 
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(1.5)
                self.player02.score +=1

            elif 'Sp' in gesture_b:
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(1.5)
                self.player02.score +=1

            else:
                print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                time.sleep(1.5)
                self.player01.score +=1

        elif 'L' in gesture_a:
                if 'R' in gesture_b: 
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(1.5)
                    self.player02.score +=1

                elif 'S' in gesture_b:
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(1.5)
                    self.player02.score =+1
                else:
                    print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                    time.sleep(1.5)
                    self.player01.score +=1

        elif 'Sp' in gesture_a:
                if 'P' in gesture_b: 
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(1.5)
                    self.player02.score +=1

                elif 'L' in gesture_b:
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(1.5)
                    self.player02.score +=1

                else:
                    print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                    time.sleep(1.5)
                    self.player01.score +=1
    def display_winner(self):
        if self.player01.score == 2:
            print(f'{self.player01.name} player 1 won!!!!!\n')
            
        else: 
            print(f'{self.player02.name} player 2 won!!!!!\n') 
    
    def restart(self):
        self.play_again = input('run it back? y or n: ').lower()
        if self.play_again == 'y':
            self.player01.score = 0
            self.player02.score = 0
            self.run_game()
        elif self.play_again == 'n':
            print('thank you come again!')
        else:
            print('invalid input please, choose y or n!')
            self.restart()