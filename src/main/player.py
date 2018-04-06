class Player:
    """

    """
    def __init__(self, name):
        self._name = name
        self._square = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, new_square):
        self._square = new_square
