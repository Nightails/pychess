from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from src.core.gamestate import GameState
from src.core.board import Board
from src.ui.board import CheckerBoard


class PyChess:
    console = Console()

    def __init__(self):
        self.gamestate = GameState()
        self.board = Board()
        self.board_ui = CheckerBoard()

    def run(self):
        text = Text(self.board_ui.board_layout(), justify="center")
        panel = Panel(text, title="PyChess")
        self.console.print(panel)
