from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board import CheckerBoard


class PyChess:
    def __init__(self):
        self.gamestate = GameState()
        self.board = Board()
        self.board_ui = CheckerBoard()

    def run(self):
        print("Running PyChess...")
        self.board_ui.draw()
        input(":")
