from enum import Enum
from pygame.math import Vector2


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
    def __init__(self, name: Name, color: Color, position: Vector2, direction: Vector2):
        self.name = name
        self.color = color
        self.position = position

    def __repr__(self):
        return f"{self.color.value} {self.name.value} at {self.position}"


class Pawn(Piece):
    def __init__(self, color: Color, position: Vector2, direction: Vector2):
        super().__init__(Name.PAWN, color, position, direction)


class Bishop(Piece):
    def __init__(self, color: Color, position: Vector2, direction: Vector2):
        super().__init__(Name.BISHOP, color, position, direction)


class Knight(Piece):
    def __init__(self, color: Color, position: Vector2, direction: Vector2):
        super().__init__(Name.KNIGHT, color, position, direction)


class Rook(Piece):
    def __init__(self, color: Color, position: Vector2, direction: Vector2):
        super().__init__(Name.ROOK, color, position, direction)


class Queen(Piece):
    def __init__(self, color: Color, position: Vector2, direction: Vector2):
        super().__init__(Name.QUEEN, color, position, direction)


class King(Piece):
    def __init__(self, color: Color, position: Vector2, direction: Vector2):
        super().__init__(Name.KING, color, position, direction)
