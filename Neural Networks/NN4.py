import sys; args = sys.argv[1:]
import math
global WEIGHTS

def nnetTrans(squareItem):
    squareItem = nnetSqr(squareItem)
    netItem = [1 for i in range(0, len(squareItem) + 1)]
    netItem[0] = 3
    for i in range(0, len(squareItem) - 1):
        netItem[i + 1] = squareItem[i + 1] * 2
    return netItem


def nnetSqr(sqr):
    sqr2 = [1 for i in range(len(sqr))]
    sqr2[0] = 2
    for i in range(0, len(sqr) - 1):
        sqr2[i + 1] = int(len(sqr[i]) / sqr2[i])
    return sqr2


def nnetOperate(sqr, netSqr, posneg, rad):
    WEIGHTS = []
    inpts = []
    item = iter(sqr[0])
    for i in range(0, netSqr[1]):
        inpts += [next(item), 0, next(item)]
    item = iter(sqr[0])
    for i in range(netSqr[1]):
        inpts += [0, next(item), next(item)]
    WEIGHTS.append(inpts)
    for j in range(2, len(netSqr)):
        n = netSqr[j - 1]
        item = iter(sqr[j - 1])
        listMaker = []

        for i in range(0, netSqr[j]):
            for k in range(0, n):
                listMaker += [next(item)]
            listMaker += [0] * n
        item = iter(sqr[j - 1])

        for i in range(0, netSqr[j]):
            listMaker += [0] * n
            for k in range(n):
                listMaker += [next(item)]
        WEIGHTS.append(listMaker)

    if posneg == "<" or posneg == " <=":
        WEIGHTS.append([((-1 * i) / (rad)) for i in sqr[-1]] * 2)
        WEIGHTS.append([0.5 / (1 / (1 + (math.exp(1))))])
    else:
        WEIGHTS.append([((i) / (rad)) for i in sqr[-1]] * 2)
        WEIGHTS.append([0.5 / (1 / (1 + (math.exp(-1))))])

    return WEIGHTS


def printCounts(weights, nnet):
    weightItems = ""
    for l in weights:
        layerItems = ""
        for w in l:
            layerItems += str(w) + " "
        weightItems += layerItems.strip() + "\n"
    layCounter = ""
    for l in nnet:
        layCounter += str(l) + " "
    print("Layer counts: " + layCounter + "1" + "\n")
    print(weightItems)

def tester(x):
  try:
    float(x)
    return True
  except ValueError:
    return False

def main():
    global WEIGHTS
    WEIGHTS = []
    sqrList = []
    with open(args[0]) as file:
        for line in file:
            if line:
                listSep = line.strip().split(", ")
                if not tester(listSep[0]):
                    continue
                else:
                    addToList = [float(e) for e in listSep]
                    sqrList.append(addToList)

    inpts = args[1].strip()
    inptsStrp = inpts[7:]
    if inptsStrp[0:2] == "<=" or inptsStrp[0:2] == ">=":
        posneg = inptsStrp[0:2]
        number = float("".join(inptsStrp[2:]))
    else:
        posneg = inptsStrp[0:1]
        number = float("".join(inptsStrp[1:]))
    e = (posneg, number)

    nnet = nnetTrans(sqrList)
    WEIGHTS = nnetOperate(sqrList, nnetSqr(sqrList), e[0], e[1])
    print(e[1])
    printCounts(WEIGHTS, nnet)


if __name__ == "__main__":
    main()

# Pooja Somayajula, 4, 2024
