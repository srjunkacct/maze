from Key import Key


class KeySpace:

    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.keys = self.createAllKeys()

    def createAllKeys(self):
        allKeys = []
        for i in range(0, self.numRows):
            for j in range(0, self.numCols):
                allKeys.append( Key(i, j))
        return allKeys

    def getAllKeys(self):
        return self.keys

    def isLegalKey(self, key):
        return ( key.row in range(0, self.numRows ) ) and ( key.col in range(0, self.numCols) )

