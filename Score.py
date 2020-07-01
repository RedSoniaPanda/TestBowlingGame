class Score:
    def __init__(self):
        self.current_score = 0
        self.total_score = 0

    def get_current_score(self):
        return self.current_score

    def add_roll_to_score(self, roll):
        self.current_score += roll
