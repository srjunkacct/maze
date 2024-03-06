

class Key:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        if self.row != other.row:
            return False
        if self.col == other.col:
            return True

    def __str__(self):
        return f"({self.row},{self.col})"

    def __hash__(self):
        return self.row * 24601 * self.col
