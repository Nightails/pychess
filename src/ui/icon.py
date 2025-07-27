empty_square = "   "
white_square = "[ ]"
black_square = "[#]"
number_squares = [f" {i} " for i in range(1, 9)]
letter_squares = [" a ", " b ", " c ", " d ", " e ", " f ", " g ", " h "]
pieces = {
    "black": {
        "king": "[♔]",
        "queen": "[♕]",
        "rook": "[♖]",
        "bishop": "[♗]",
        "knight": "[♘]",
        "pawn": "[♙]",
    },
    "white": {
        "king": "[♚]",
        "queen": "[♛]",
        "rook": "[♜]",
        "bishop": "[♝]",
        "knight": "[♞]",
        "pawn": "[♟]",
    },
}
