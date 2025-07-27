from pygame.math import Vector2
from src.core.piece import Color, Pawn, Rook, Knight, Bishop, Queen, King
from src.core.util import text_to_coordinates


class Board:
    pieces: list = []  # track pieces currently on board
    layout: dict = {}  # track currently occupied spaces

    def __init__(self):
        # spawning pieces
        self.pieces.extend(init_pieces(Color.WHITE))
        self.pieces.extend(init_pieces(Color.BLACK))

        # board layout
        self.layout = init_board_layout(self.pieces)

    def move_piece(self, cmd: str, is_white_turn: bool) -> bool:
        # parse text to chess commend - from coordinate, to coordinate
        coords = text_to_coordinates(cmd)
        if coords is None or type(coords) is not tuple:
            return False

        # find the piece at given coordinate
        piece = self.layout[coords[0].x, coords[0].y]
        if piece is None:
            return False

        # only move pieces on their turn
        if is_white_turn and piece.color is Color.BLACK:
            return False
        if not is_white_turn and piece.color is Color.WHITE:
            return False

        # todo: check new position is valid, according to piece's move rule

        # move that piece to new position and update the layout
        piece.position = coords[1]
        self.layout[int(piece.position.x), int(piece.position.y)] = piece
        del self.layout[coords[0].x, coords[0].y]

        return True


def init_pieces(color: Color) -> list:
    pieces = []

    # White facing up and Black facing down
    dir = Vector2(0, 1) if color is Color.WHITE else Vector2(0, -1)

    # pawns
    for x in range(1, 9):
        y = 2 if color is Color.WHITE else 7
        pos = Vector2(x, y)
        pieces.append(Pawn(color, pos, dir))

    y = 1 if color is Color.WHITE else 8
    # rooks
    pieces.append(Rook(color, Vector2(1, y), dir))
    pieces.append(Rook(color, Vector2(8, y), dir))
    # knights
    pieces.append(Knight(color, Vector2(2, y), dir))
    pieces.append(Knight(color, Vector2(7, y), dir))
    # bishops
    pieces.append(Bishop(color, Vector2(3, y), dir))
    pieces.append(Bishop(color, Vector2(6, y), dir))
    # queen
    pieces.append(Queen(color, Vector2(4, y), dir))
    # king
    pieces.append(King(color, Vector2(5, y), dir))

    return pieces


def init_board_layout(pieces: list) -> dict:
    board = {}
    for piece in pieces:
        board[int(piece.position.x), int(piece.position.y)] = piece
    return board
