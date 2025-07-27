from textual import on
from textual.app import App
from textual.containers import Container, Horizontal

from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board_panel import BoardPanel
from src.ui.panel import StatusPanel, LogPanel, InfoPanel, CMDPanel


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
        self.make_move(cmd.value)
        cmd.value = ""

    def make_move(self, move: str):
        if self.board.move_piece(move, self.gamestate.is_white_turn):
            board = self.query_one(BoardPanel)
            board.update_board(self.board.layout)
            self.update_turn()
            log = self.query_one(LogPanel)
            log.update_log(move)

    def update_turn(self):
        self.gamestate.next_turn()
        status = self.query_one(StatusPanel)
        status.update(self.gamestate.get_turn())
