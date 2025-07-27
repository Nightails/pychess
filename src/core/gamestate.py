class GameState:
    def __init__(self):
        self.is_white_turn: bool = True
        # todo: chess clock for both sides

    def next_turn(self):
        self.is_white_turn = not self.is_white_turn

    def get_turn(self):
        return "White Turn" if self.is_white_turn else "Black Turn"
