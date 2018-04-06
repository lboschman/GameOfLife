class Square:
    """ Govern the properties of different squares on a board
    """
    def __init__(self, index):
        self.index = index


class Board:
    """ Govern the properties of an entire playing board for the game
    """
    def __init__(self, number_squares):
        self._number_squares = number_squares
