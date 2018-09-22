import game_API
import math

def logEvaluator(attributeDictionary):
    # attribute dictionary format:
    # {health : {original : ? , change: ? , weight: ? },
    # rock : {original : ? , change: ? , weight: ? }}
    totalScore = 0
    for key, value in attributeDictionary.items():
        newValue = value['original'] + value['change']
        score = value['weight'] * logNoError(newValue/value['original'])
        totalScore += score
    return totalScore

def logNoError(x):
    if x > 0:
        return math.log(x)
    else:
        return -math.inf

testDict = {"health" : {"original" : 100, "change" : 0, "weight" : 5},
            "rock": {"original": 3, "change": 2, "weight": 1}}
print(logEvaluator(testDict))
