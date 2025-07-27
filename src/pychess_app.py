from textual.app import App, RenderResult
from textual.containers import Horizontal

from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board_panel import BoardPanel
from src.ui.info_panel import InfoPanel
from src.ui.log_panel import LogPanel
from src.ui.cmd_panel import CMDPanel


class PyChess(App):
    gamestate = GameState()
    board = Board()

    CSS = """
    Screen {
        background: black;
    }
    """

    def on_mount(self) -> None:
        self.screen.border_title = "PyChess"
        self.screen.styles.border = ("double", "white")

    def compose(self) -> RenderResult:
        self.info_panel = InfoPanel()
        self.board_panel = BoardPanel()
        self.board_panel.update_board(self.board.layout)
        self.log_panel = LogPanel()
        self.cmd_ui = CMDPanel()

        yield Horizontal(
            self.info_panel,
            self.board_panel,
            self.log_panel,
        )
        yield self.cmd_ui
