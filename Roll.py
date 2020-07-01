class Roll:
    def __init__(self):
        self.current_roll = 0
        self.num_balls_rolled = {}

    def get_current_roll(self):
        return self.current_roll

    def get_number_balls_hit(self):
        return self.num_balls_rolled[self.current_roll]

    def roll_once(self, number_balls_rolled):
        self.current_roll += 1
        self.num_balls_rolled[self.current_roll] = number_balls_rolled
