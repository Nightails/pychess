from textual.app import App, RenderResult

from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board import CheckerBoard


class PyChess(App):
    gamestate = GameState()
    board = Board()

    def on_mount(self) -> None:
        self.screen.border_title = "PyChess"
        self.screen.styles.border = ("double", "white")

    def compose(self) -> RenderResult:
        self.board_ui = CheckerBoard()
        self.board_ui.update_board(self.board.layout)
        yield self.board_ui
