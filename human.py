from player import Player



class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = ''

    def create_players(self):
      player_name = input()
      return player_name
