import unittest

from Action import Action
from ActionSpace import ActionSpace
from Key import Key
from KeySpace import KeySpace
from Maze import Maze
from Policy import Policy


class MyTestCase(unittest.TestCase):

    def policyValueToString(self, policyMap):
        returnVal = ""
        if policyMap == None:
            return returnVal
        for key in policyMap.keys():
            returnVal = returnVal + (f"({str(key)}, {str(policyMap[key])}) ")
        return returnVal


    def test_something(self):
        print("")
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
        newPolicy, delta = policy.revisePolicy( newValueMap )
        while delta > 0.001:
            newValueMap = newPolicy.evaluate()
            newPolicy, delta = newPolicy.revisePolicy( newValueMap )
        for key in keySpace.getAllKeys():
            print(f"Key = {key} value = {newValueMap[key]} policy = { self.policyValueToString(newPolicy.policyMap[key]) }")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
