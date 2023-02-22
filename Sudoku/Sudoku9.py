import sys; args = sys.argv[1:]
import time

startTime = time.time()

with open(args[0]) as f:
  listpuzz = [line.strip() for line in f]


def setGlobals():
    global SIDELEN, BLOCKS, ROWS, COLS, QUEENS, NBRS
    SIDELEN = int(81**.5)
    ROWS = [{j for j in range(i, i + SIDELEN)} for i in range(0, 81, SIDELEN)]
    COLS = [{j for j in range(i, 81, SIDELEN)} for i in range(0, SIDELEN)]
    BLOCKS = [{0, 1, 2, 9, 10, 11, 18, 19, 20},
              {3, 4, 5, 12, 13, 14, 21, 22, 23},
              {6, 7, 8, 15, 16, 17, 24, 25, 26},
              {27, 28, 29, 36, 37, 38, 45, 46, 47},
              {30, 31, 32, 39, 40, 41, 48, 49, 50},
              {33, 34, 35, 42, 43, 44, 51, 52, 53},
              {54, 55, 56, 63, 64, 65, 72, 73, 74},
              {57, 58, 59, 66, 67, 68, 75, 76, 77},
              {60, 61, 62, 69, 70, 71, 78, 79, 80}
              ]

    QUEENS = {*'123456789'}
    NBRS = []
    for i in range(0, 81):
        for j in ROWS:
            if i in j:
                tR = j
        for j in COLS:
            if i in j:
                tC = j
        for j in BLOCKS:
            if i in j:
                tB = j
        x = tR|tC|tB
        x.remove(i)
        NBRS.append(x)

def makeBest(pzl):
    global BESTOPTION
    BESTOPTION = {}
    for i in range(0, 81):
        if pzl[i] == '.':
            BESTOPTION[i] = QUEENS - {pzl[j] for j in NBRS[i]}

def checksum(pzl):
    return str(sum([ord(i) - ord("1") for i in pzl]))

def findMin(dictOps):
    return min(dictOps.items(), key=lambda x: len(x[1]))

def updateBest(pzl, indChanged, newDict):
    del newDict[indChanged[0]]
    for i in newDict:
        if i in NBRS[indChanged[0]]:
            newDict[i] = QUEENS - {pzl[j] for j in NBRS[i]}

    mini = findMin(newDict)
    return mini, newDict

def bruteForce(pzl, dotIndex, bestOptions):
    if "." not in pzl:
        return pzl
    copyIt = {key: value for key, value in bestOptions.items()} # keep a copy of dictionary
    if pzl[dotIndex[0]] != '.':
        dotIndex, copyIt = updateBest(pzl, dotIndex, copyIt) # find dot with least number of choices, and changed dictionary
    for choice in dotIndex[1]:
        subPzl = pzl[:dotIndex[0]] + choice + pzl[dotIndex[0]+1:]
        bF = bruteForce(subPzl, dotIndex, copyIt)
        if bF:
            return bF
    return ""

def isInvalid(pzl, ind):
    if pzl[ind] in {pzl[i] for i in NBRS[ind] if pzl[i] != '.'}:
        return True
    return False

def main():
    counter = 0
    setGlobals()
    for p in listpuzz:
        makeBest(p)
        counter+=1
        len1 = len(str(counter))
        print(str(counter) + ": " + p)
        sol = bruteForce(p, findMin(BESTOPTION), BESTOPTION)
        time1 = "{0:.4g}".format(time.time() - startTime)
        print(" "*len1 + "  " + sol + " " + checksum(sol) + " " + time1 + "s")

if __name__ == '__main__':
    main()

# Pooja Somayajula, 4, 2024
