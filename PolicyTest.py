import unittest

from Action import Action
from ActionSpace import ActionSpace
from Key import Key
from KeySpace import KeySpace
from Maze import Maze
from Policy import Policy


class MyTestCase(unittest.TestCase):
    def test_something(self):
        keySpace = KeySpace(4,4)
        actions = [ Action(-1,0), Action(1,0), Action(0,-1), Action(0,1)]
        actionSpace = ActionSpace(actions)
        maze = Maze( keySpace, actionSpace, [Key(0,0), Key(3,3)])
        initialPolicyMap = {}
        for key in keySpace.getAllKeys():
            if key in maze.goal:
                initialPolicyMap[key] = None
            else:
                actions = actionSpace.getLegalActions(key, keySpace)
                probability = 1.0 / len(list(actions))
                actionDistribution={}
                for action in actions:
                    actionDistribution[action] = probability
                initialPolicyMap[key] = actionDistribution
        policy = Policy(maze, initialPolicyMap )
        newValueMap = policy.evaluate()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
