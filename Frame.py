from Roll import Roll


class Frame:
    _NUMBER_OF_FRAMES = 10

    def __init__(self):
        self.number_of_frames = self._NUMBER_OF_FRAMES
        self.roll = Roll()

    def get_number_frames_left(self):
        return self.number_of_frames

    def decrement_number_frames(self):
        if (self.roll.get_current_roll() % 2) is 0:
            self.number_of_frames -= 1
        elif self.roll.get_number_balls_hit() is 10:
            self.roll.roll_once(0)
            self.number_of_frames -= 1

    def roll_once(self, number_balls_rolled):
        self.roll.roll_once(number_balls_rolled)
        self.decrement_number_frames()
