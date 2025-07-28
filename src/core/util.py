from pygame.math import Vector2

NUMLETTER = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}


def text_to_positions(text: str):
    # convert text base command to (x,y) coordinate
    pos_0 = (text[0], text[1])
    pos_1 = (text[2], text[3])

    # check for out of bound position
    if not is_valid_position(pos_0) or not is_valid_position(pos_1):
        # todo: send out error
        return None

    # convert pos[0] to digit
    vec_0 = Vector2(NUMLETTER[pos_0[0]], int(pos_0[1]))
    vec_1 = Vector2(NUMLETTER[pos_1[0]], int(pos_1[1]))
    return vec_0, vec_1


def is_valid_position(position: list) -> bool:
    if position[0].isalpha() and position[1].isdigit():
        if position[0] in NUMLETTER and (int(position[1]) > 0 and int(position[1]) < 9):
            return True
    return False
