
class Maze:

    def __init__(self, keySpace, actionSpace, goal):
        self.keySpace = keySpace
        self.actionSpace = actionSpace
        self.goal = goal

    def getLegalActions(self, key):
        return self.actionSpace.getLegalActions( key, self.keySpace )