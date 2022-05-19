from human import Human

class Player:
    def __init__(self, name):
        self.name = name
        self.possible_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.chosen_gesture = ''
        self.current_score = 0


    def choose_gesture(self):
        
        
        while True:
            try:
                chosen_gesture = int(input('please provide your gesture'))
            except ValueError:
                print('Sorry that is not a valid gesture, Please chose again')
                continue

            if chosen_gesture >= 5:
                print('invalid gesutre. Try Again')
            else:
                return chosen_gesture