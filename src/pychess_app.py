from textual.app import App
from textual.containers import Horizontal

from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board_panel import BoardPanel
from src.ui.info_panel import InfoPanel
from src.ui.log_panel import LogPanel
from src.ui.cmd_panel import CMDPanel


class PyChess(App):
    CSS = """
    Screen {
        background: black;
    }
    """

    def __init__(self):
        super().__init__()
        self.gamestate = GameState()
        self.board = Board()
        self.input = ""

    def on_mount(self):
        self.screen.border_title = "PyChess"
        self.screen.styles.border = ("double", "white")

    def compose(self):
        self.info_panel = InfoPanel()
        self.board_panel = BoardPanel()
        self.board_panel.update_board(self.board.layout)
        self.log_panel = LogPanel()
        self.cmd_panel = CMDPanel()

        yield Horizontal(
            self.info_panel,
            self.board_panel,
            self.log_panel,
        )
        yield self.cmd_panel
