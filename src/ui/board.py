from src.ui import icon


class CheckerBoard:
    def __init__(self):
        self.squares = []
        self.init_squares()

    def board_layout(self):
        lines = []
        for r in range(len(self.squares)):
            lines.append("".join(self.squares[r]))
        return "\n".join(lines)

    def init_squares(self):
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

    def init_pieces(self):
        pass
