import math
import random

totalScore = {}
totalLen = {}

def bandit(testNum, armIdx, pullVal):
    global totalScore, totalLen
    c = 1.00000000001
    if testNum == 0:
        totalScore = {i: 0 for i in range(armIdx)}
        totalLen = {i: 0 for i in range(armIdx)}
    else:
        totalScore[armIdx] += pullVal
        totalLen[armIdx] += 1
    if testNum <= 9:
        return testNum % 10
    else:
        countScore = []
        for i in range(0, 10):
            score = (totalScore[i] / totalLen[i] + 0.85 * (c ** testNum) * ((math.log(testNum)/totalLen[i]) ** 0.5))
            countScore.append(score)
        maxScore = max(countScore)
        return countScore.index(maxScore)

# Pooja Somayajula, 4, 2024
