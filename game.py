import random
from human import Human
from ai import Ai
from player import Player
import random, time, sys



class Game:
    def __init__(self):
        self.player1 = Human(input('hello player1, what is your name?  '))
        self.player2 = Ai('opponent')
        pass
    def run_game(self):
        self.display_rules()
        self.is_opponent_human_or_ai()
        self.get_names()
        play_status = True
        while(play_status == True):
            self.start_rounds()
            self.display_game_winner()
            play_status = self.play_again()
    
    def display_welcome(self):
        print ('Welcome to the best classic game ever of Rock, Paper, Scissors, Lizard, Spock!')
    def display_rules(self):
        print('The game will be played as best two out of three games!')
        print('rock destroys scissors!')
        print('scissors cuts paper!')
        print ('paper covers Rock!')
        print('rock kills Lizard!') 
        print('Lizard poisons spock!')
        print('spock destroys scissors!')
        print('scissors kills Lizard!')
        print('Lizard eats paper!')
        print('spock burns paper!')
        print('spock smashes rock!')
        print('rock kills spock!')

    def is_opponent_human_or_ai(self):
        valid_multi_input = self.validate_yes_no('multiplayer')
        if valid_multi_input == 'y':
            pass
        else:
            self.opponent = Ai()

            


while True: # Main game loop.
    while True: # Keep asking until player enters R, P, S, L, S, or Q.
        print("{} Wins, {} Losses, {} Ties'.format('wins, losses, ties')")
        print("Enter your move: (R)ock (P)aper (S)cissors (L)izard (SP)ock or (Q)uit")
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S' or playerMove == 'L' or playerMove == 'SP':
            break
        else:
            print('Type one of R, P, S, L, SP, Q')

    # Display what the player chose:
    if playerMove == 'R':
        print('ROCK versus.')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus.')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus.')
        playerMove = 'SCISSORS'
    elif playerMove == 'L':
        print('Lizard versus.')
        playerMove = 'LIZARD'
    elif playerMove == 'SP':
        print('Spock versus.')
        playerMove = 'SPOCK'

    # Count to three with dramatic pauses:
    time.sleep(2)
    print('1...')
    time.sleep(2)
    print('2...')
    time.sleep(2)
    print('3...')
    time.sleep(2)

    # Display what the ai chose:
    randomNumber = random.randint(0, 4)
    if randomNumber == 0:
        AiMove = 'ROCK'
    elif randomNumber == 1:
        AiMove = 'PAPER'
    elif randomNumber == 2:
        AiMove = 'SCISSORS'
    elif randomNumber == 3:
        AiMove = 'LIZARD'
    elif randomNumber == 4:
        AiMove = 'SPOCK'
    print( AiMove)
    time.sleep(2)

    # Display and record the win/loss/tie:
    # if self.player_one.chosen_gesture == 'ROCK' and self.player_two.chosen_gesture == 'PAPER'
    # self.player_two.wins += 1
    if playerMove == AiMove:
        print('It\'s a tie!')
        ties = 'ties + 1'
    elif playerMove == 'ROCK' and AiMove == 'SCISSORS':
        print('You win!')
        wins = 'wins += 1'
    elif playerMove == 'PAPER' and AiMove == 'ROCK':
        print('You win!')
        wins = 'wins += 1'
    elif playerMove == 'SCISSORS' and AiMove == 'PAPER':
        print('You win!')
        wins = 'wins += 1'
    elif playerMove == 'LIZARD' and AiMove == 'PAPER':
        print('You win!') 
        wins = 'wins += 1'
    elif playerMove == 'LIZARD' and AiMove == 'ROCK':
        print('You win!')
        wins = 'wins += 1'
    elif playerMove == 'LIZARD' and AiMove == 'SPOCK':
        print('You win!')
        wins = 'wins += 1'
    elif playerMove == 'SPOCK' and AiMove == 'ROCK':
        print('You win!')
        wins = 'wins += 1'
    elif playerMove == 'SPOCK' and AiMove == 'PAPER':
        print('You win!')
        wins = 'wins += 1'
    elif playerMove == 'SPOCK' and AiMove == 'SCISSORS':
        print('You win!')
        wins = 'wins + 1'
    elif playerMove == 'SPOCK' and AiMove == 'LIZARD':
        print('You win!')
        wins = 'wins + 1'
    elif playerMove == 'ROCK' and AiMove == 'SPOCK':
        print('You win!')
        wins = 'wins + 1'   
    elif playerMove == 'ROCK' and AiMove == 'LIZARD':
        print('You win!')
        wins = 'wins + 1'
    elif playerMove == 'PAPER' and AiMove == 'SPOCK':
        print('You win!')
        wins = 'wins + 1'  
    elif playerMove == 'SCISSORS' and AiMove == 'LIZARD':
        print('You win!')
        wins = 'wins + 1'
    elif playerMove == 'SCISSORS' and AiMove == 'SPOCK':
        print('You win!')
        wins = 'wins + 1'


    elif playerMove == 'ROCK' and AiMove == 'PAPER':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'PAPER' and AiMove == 'SCISSORS':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'SCISSORS' and AiMove == 'ROCK':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'ROCK' and AiMove == 'LIZARD':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'ROCK' and AiMove == 'SPOCK':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'PAPER' and AiMove == 'LIZARD':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'PAPER' and AiMove == 'SPOCK':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'SCISSORS' and AiMove == 'LIZARD':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'SCISSORS' and AiMove == 'SPOCK':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'LIZARD' and AiMove == 'ROCK':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'LIZARD' and AiMove == 'PAPER':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'LIZARD' and AiMove == 'SPOCK':
        print('You lose!')
        losses = 'losses += 1'
    elif playerMove == 'LIZARD' and AiMove == 'SCISSORS':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'SPOCK' and AiMove == 'ROCK':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'SPOCK' and AiMove == 'PAPER':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'SPOCK' and AiMove == 'SCISSORS':
        print('You lose!')
        losses = 'losses + 1'
    elif playerMove == 'SPOCK' and AiMove == 'LIZARD':
        print('You lose!')
        losses = 'losses + 1'

def confirm_rpsls(Game):
    thank_you_message = 'Thank you for playing rpsls!'

    print(f'Did you like playing rpsls!')
    user_input = input(f'Are you satisfied with playing the new rock, paper, scissors? yes or no:')
    if user_input == 'yes':
        print(thank_you_message)
    else:
        if user_input == 'no':
            new_age_rpsls()


new_school_game_of_rpsls()
