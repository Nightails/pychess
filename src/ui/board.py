from textual.widgets import Static
from src.ui import icon


class CheckerBoard(Static):
    squares = []
    layout = {}

    DEFAULT_CSS = """
    CheckerBoard {
        content-align: center middle;
    }
    """

    def __init__(self):
        super().__init__()
        self.border_title = "Board"
        self.styles.border = ("round", "white")

    def update_board(self, layout: dict) -> None:
        self.layout = layout
        self.draw_board()
        self.draw_pieces()
        content = self.layout_to_text()
        self.update(content)

    def draw_board(self) -> None:
        row = []
        for r in range(9):
            column = []
            for c in range(9):
                if r == 0 and c == 0:
                    column.append(icon.empty_square)
                elif r > 0 and c == 0:
                    column.append(icon.number_squares[r - 1])
                elif r == 0 and c > 0:
                    column.append(icon.letter_squares[c - 1])
                elif (r + (c % 2)) % 2 == 0:
                    column.append(icon.black_square)
                else:
                    column.append(icon.white_square)
            row.append(column)
        self.squares = row

    def draw_pieces(self) -> None:
        for key in self.layout.keys():
            piece = self.layout[key]
            color = piece.color.value
            name = piece.name.value
            piece_icon = icon.pieces[color][name]
            self.squares[key[1]][key[0]] = piece_icon

    def layout_to_text(self) -> str:
        lines = []
        for r in range(len(self.squares)):
            lines.append("".join(self.squares[r]))
        return "\n".join(lines)
