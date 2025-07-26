from enum import Enum
from vectormath import Vector2


class Color(Enum):
    BLACK = "black"
    WHITE = "white"


class Name(Enum):
    PAWN = "pawn"
    BISHOP = "bishop"
    KNIGHT = "knight"
    ROOK = "rook"
    QUEEN = "queen"
    KING = "king"


class Piece:
    def __init__(self, name: Name, color: Color, position: Vector2):
        self.name = name
        self.color = color
        self.position = position

    def __repr__(self):
        return f"{self.color} {self.name} at {self.position}"


class Pawn(Piece):
    def __init__(self, color: Color, position: Vector2):
        super().__init__(Name.PAWN, color, position)


class Bishop(Piece):
    def __init__(self, color: Color, position: Vector2):
        super().__init__(Name.BISHOP, color, position)


class Knight(Piece):
    def __init__(self, color: Color, position: Vector2):
        super().__init__(Name.KNIGHT, color, position)


class Rook(Piece):
    def __init__(self, color: Color, position: Vector2):
        super().__init__(Name.ROOK, color, position)


class Queen(Piece):
    def __init__(self, color: Color, position: Vector2):
        super().__init__(Name.QUEEN, color, position)


class King(Piece):
    def __init__(self, color: Color, position: Vector2):
        super().__init__(Name.KING, color, position)
