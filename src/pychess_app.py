from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board import CheckerBoard


class PyChess:
    gamestate = GameState()
    board = Board()
    board_ui = CheckerBoard(board.layout)

    def run(self):
        console = Console()

        board_layout = Text(self.board_ui.board_layout(), justify="center")
        board_panel = Panel(board_layout, title="PyChess")
        console.print(board_panel)

        cmd = Prompt.ask("Move")
