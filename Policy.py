
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




