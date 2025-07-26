from textual.app import App, ComposeResult
from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board import CheckerBoard


class PyChess(App):
    def __init__(self):
        super().__init__()
        self.gamestate = GameState()
        self.board = Board()

    def compose(self) -> ComposeResult:
        yield CheckerBoard(6)
