from Key import Key


class Action:

    def __init__(self, deltaRow, deltaCol):
        self.deltaRow = deltaRow
        self.deltaCol = deltaCol

    def act(self, key):
        return ( Key( key.row + self.deltaRow, key.col + self.deltaCol ), -1 )
