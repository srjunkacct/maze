
import random

class Policy:

    def __init__(self, maze, policyMap):
        self.maze = maze
        self.policyMap = policyMap
        self.errorThreshold = 0.001

    def initialValueMap(self):
        valueMap = {}
        for key in self.policyMap.keys():
            valueMap[key] = 0.0
        return valueMap

    def evaluateOnce(self, valueMap):
        delta = 0.0
        newValueMap = valueMap.copy()
        for key in self.policyMap.keys():
            actionDistribution = self.policyMap[key]
            if actionDistribution == None:
                continue
            newValue = 0.0
            for action in actionDistribution.keys():
                newKey, reward = action.act(key)
                newValue += ( valueMap[newKey] + reward ) * actionDistribution[action]
            newValueMap[key] = newValue
            delta = max(delta, abs( newValue - valueMap[key]) )
        return delta, newValueMap


    def evaluate(self):
        valueMap = self.initialValueMap()
        delta, newValueMap = self.evaluateOnce(valueMap)
        while delta > self.errorThreshold:
            delta, newValueMap = self.evaluateOnce(newValueMap)
        return newValueMap

    def revisePolicy(self, valueMap):
        delta = 0.0
        revisedPolicyMap = {}
        for key in valueMap.keys():
            if key in self.maze.goal:
                revisedPolicyMap[key] = None
                continue
            validActions = self.maze.getLegalActions(key)
            actionOutcomes = [ action.act(key) for action in validActions ]
            actionValues = [ outcome[1] + valueMap[outcome[0]] for outcome in actionOutcomes ]
            bestActionValue = max(actionValues)
            bestIndex = actionValues.index(bestActionValue)
            bestActions = [ action for action in validActions if abs( (action.act(key))[1] + valueMap[(action.act(key))[0]] - bestActionValue )  < 0.001 ]
            numBestActions = len(bestActions)
            probability = 1.0 / numBestActions
            policy = {}
            for action in bestActions:
                policy[action] = probability
                delta = max( delta, abs( valueMap[key] - bestActionValue ))
            revisedPolicyMap[key] = policy
        return Policy( self.maze, revisedPolicyMap ), delta





