from textual import on
from textual.app import App
from textual.containers import Container, Horizontal

from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board_panel import BoardPanel
from src.ui.info_panel import InfoPanel
from src.ui.log_panel import LogPanel
from src.ui.cmd_panel import CMDPanel
from src.ui.panel import StatusPanel


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

    def on_mount(self):
        self.screen.border_title = "PyChess"
        self.screen.styles.border = ("double", "white")

    def compose(self):
        yield Container(
            StatusPanel(self.gamestate.get_turn()),
            Horizontal(
                InfoPanel(),
                BoardPanel(self.board.layout),
                LogPanel(),
            ),
            CMDPanel(),
        )

    @on(CMDPanel.Submitted)
    def cmd_to_move(self):
        cmd = self.query_one(CMDPanel)
        log = self.query_one(LogPanel)
        log.update_log(cmd.value)
        self.update_turn()
        cmd.value = ""

    def update_turn(self):
        self.gamestate.next_turn()
        status = self.query_one(StatusPanel)
        status.update(self.gamestate.get_turn())
