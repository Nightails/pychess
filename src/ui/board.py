from textual.widget import Widget
from textual.strip import Strip
from rich.segment import Segment


class CheckerBoard(Widget):
    COMPONENT_CLASSES = {
        "checkerboard--white-cell",
        "checkerboard--black-cell",
    }

    DEFAULT_CSS = """
    CheckerBoard .checkerboard--white-cell {
    background: #eeeed2;
    }
    CheckerBoard .checkerboard--black-cell {
    background: #769656;
    }
    """

    def __init__(self, cellsize: int):
        super().__init__()
        self.cellsize = cellsize

    def render_line(self, y: int) -> Strip:
        row_index = y // (self.cellsize / 2)
        if row_index >= 8:
            return Strip.blank(self.size.width)

        # todo: replace with css
        white = self.get_component_rich_style("checkerboard--white-cell")
        black = self.get_component_rich_style("checkerboard--black-cell")

        is_odd = row_index % 2

        segments = [
            Segment(" " * self.cellsize, black if (column + is_odd) % 2 else white)
            for column in range(8)
        ]

        strip = Strip(segments)
        return strip
