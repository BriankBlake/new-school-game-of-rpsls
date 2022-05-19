import random
from human import Human
from ai import Ai
from player import Player
import random, time, sys

class Game:
   while True: # Main game loop.
    while True: # Keep asking until player enters R, P, S, L, S, or Q.
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
        print("Enter your move: (R)ock (P)aper (S)cissors (L)izard (S)pock or (Q)uit")
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S' or playerMove == 'L' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, L, S, Q')

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
        playerMove = 'Lizard'
    elif playerMove == 'S':
        print('Spock versus.')
        playerMove = 'Spock'

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the ai chose:
    randomNumber = random.randint(0, 4)
    if randomNumber == 0:
        AiMove = 'ROCK'
    elif randomNumber == 1:
        AiMove = 'PAPER'
    elif randomNumber == 2:
        AiMove = 'SCISSORS'
    elif randomNumber == 3:
        AiMove = 'Lizard'
    elif randomNumber == 4:
        AiMove = 'Spock'
    print( AiMove)
    time.sleep(0.5)

    # Display and record the win/loss/tie:
    if playerMove == AiMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif playerMove == 'ROCK' and AiMove == 'SCISSORS':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'PAPER' and AiMove == 'ROCK':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'SCISSORS' and AiMove == 'PAPER':
        print('You win!')
        wins = wins + 1

    elif playerMove == 'ROCK' and AiMove == 'PAPER':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'PAPER' and AiMove == 'SCISSORS':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'SCISSORS' and AiMove == 'ROCK':
        print('You lose!')
        losses = losses + 1