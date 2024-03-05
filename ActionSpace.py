

class ActionSpace:

    def __init__(self, actions):
        self.actions = actions

    def getLegalActions(self, key, keyspace):
        return [ action for action in  self.actions if  keyspace.isLegalKey( action.act(key)[0] ) ]


