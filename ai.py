import random 
from player import Player
from human import Human

class Ai(Human):
    def __init__(self):
        super().__init__()
        self.name = 'ai'