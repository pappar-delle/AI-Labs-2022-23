import math

totalArms = []
countArms = []
totalScore = 0


def bandit(testNum, armIdx, pullVal):
    global totalArms, countArms, totalScore
    c = 0.6
    if testNum == 0:
        totalArms = [0 for i in range(armIdx)]
        countArms = [0 for i in range(armIdx)]
        totalScore = 0
        return 0
    else:
        totalScore += 1
        countArms[armIdx] += 1
        totalArms[armIdx] = ((totalArms[armIdx] * (countArms[armIdx] - 1)) + pullVal) / countArms[armIdx]
        if testNum <= 9:
            return testNum
        else:
            score = [totalArms[i] + math.sqrt(((c * math.log(totalScore)) / countArms[i])) for i in range(10)]
            return score.index(max(score))

# Pooja Somayajula, 4, 2024
