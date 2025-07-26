class GameState:
    def __init__(self):
        self.is_white_turn: bool = True
        # todo: chess clock for both sides

    def switch_turn(self):
        self.is_white_turn = not self.is_white_turn
