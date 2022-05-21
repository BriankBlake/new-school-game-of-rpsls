import random

from player import Player



class Ai(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Ai'

    def ai_gesture(self):
        random_gesture = random.randint(0,5)
        return random_gesture
        
