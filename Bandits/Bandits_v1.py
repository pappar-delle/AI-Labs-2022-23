import math
import random

numberOfArms = 0
totalScore = list()
countScore = list()

def bandit(testNum, armIdx, pullVal):
    global totalScore, countScore, numberOfArms
    if testNum == 0:
        numberOfArms = armIdx
        totalScore = []
        countScore = []
        for i in range(numberOfArms):
            totalScore.append(0)
            countScore.append(0)
        itm = list(range(numberOfArms))
        return random.choice(itm)
    elif testNum >= 1:
        totalScore[armIdx] += 1
        countScore[armIdx] += pullVal
        result = 0
        bestResult = 0
        for i in range(numberOfArms):
            if totalScore[i] == 0:
                score = float('inf')
            else:
                score = (countScore[i] / totalScore[i])
                score += (1.3 * math.sqrt(math.log10(testNum) / totalScore[i]))
            if result < score:
                result = score
                bestResult = i
        return bestResult


# Pooja Somayajula, 4, 2024
