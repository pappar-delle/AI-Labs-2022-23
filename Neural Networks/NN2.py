import sys;args = sys.argv[1:]
import math
import random

with open(args[0]) as inpFile:
    inpList = [line.strip().split(' ') for line in inpFile]
for i in inpList:
    i.remove('=>')

iden = [[float(k) for k in i[:len(i) - 1]] for i in inpList]
targetList = [float(i[len(i) - 1]) for i in inpList]
EList = [10 for k in range(len(iden))]
tree = [[1 for k in range(len(iden[0]) + 1)], [0, 0], [0]]
weightArray = [[1 for k in range(((len(iden[0]) + 1) * 2))], [1, 1], [1]]


def transferFunc(n):
    return 1 / (1 + math.exp(-n))


def derivFunc(n):
    return n * (1 - n)


def dotProd(vector1, vector2):
    productList = []
    for k in range(len(vector1)):
        productList.append(vector1[k] * vector2[k])
    return sum(productList)


def futureNodes(inputs, wLayer):
    numItems = len(inputs)
    cells = int(len(wLayer) / numItems)
    indexList = []
    cList = []
    for i in range(cells):
        indexList.append(wLayer[i * numItems:i * numItems + numItems])
    for i in indexList:
        cList.append(transferFunc(dotProd(inputs, i)))
    return cList


def feedForward(inputs, wList):
    cellItems = inputs
    tree = []
    for chip in range(0, len(wList) - 1):
        tree.append(cellItems)
        cellItems = futureNodes(cellItems, wList[chip])
    tree.append(cellItems)
    finalWeights = wList[len(wList) - 1]
    resultList = [cellItems[i] * finalWeights[i] for i in range(len(cellItems))]
    tree.append(resultList)
    return tree, resultList


def bProp(tree, weights, target, alphaVal):
    madeWeights = [[*i] for i in weights]
    grad = [[*i] for i in weights]
    EArray = [[*nodes] for nodes in tree]
    EArray[len(EArray) - 1][0] = target - tree[len(EArray) - 1][0]
    EArray[len(EArray) - 2][0] = EArray[len(EArray) - 1][0] * weights[len(EArray) - 2][0] * derivFunc(
        tree[len(EArray) - 2][0])

    for ind in range(len(EArray) - 3, 0, -1):
        for i in range(len(EArray[ind])):
            EArray[ind][i] = derivFunc(tree[ind][i]) * dotProd(EArray[ind + 1],
                                                               [weights[ind][w] for w in range(len(weights[ind])) if
                                                                w % len(EArray[ind]) == i])

    for ind in range(0, len(tree) - 1):
        for nodeLister in range(len(tree[ind])):
            for nodeResult in range(len(tree[ind + 1])):
                grad[ind][nodeLister + nodeResult * len(tree[ind])] = EArray[ind + 1][nodeResult] * tree[ind][
                    nodeLister]

    for ind in range(0, len(madeWeights)):
        for weight in range(len(madeWeights[ind])):
            madeWeights[ind][weight] = weightArray[ind][weight] + grad[ind][weight] * alphaVal

    return madeWeights


minE = 1
minWs = []
minTester = 0
minEList = []
foofighters = []
counter = 0
counterE = 0
alphaVal = 0.1


def randomWeightMaker(weights):
    for layer in weights:
        for weight in range(len(layer)):
            layer[weight] = random.randint(-2, 2)
    return weights


weightArray = randomWeightMaker(weightArray)
for i in range(0, 300000):
    nodes = iden[i % len(iden)].copy()
    nodes.append(1)
    iNodes, result = feedForward(nodes, weightArray)

    result = result[0]
    madeWeights = bProp(iNodes, weightArray, targetList[i % len(iden)], alphaVal)
    weightArray = madeWeights
    tempNodes, findItem = feedForward(nodes, madeWeights)
    findItem = findItem[0]
    e = .5 * (targetList[i % len(iden)] - findItem) ** 2
    EList[i % len(iden)] = e
    newErr = sum(EList)

    if i - counter > 20000 and newErr - counterE < .0001:
        counter = i
        counterE = newErr
        weightArray = randomWeightMaker(weightArray)
    counter = 0

    if newErr < minE and i - counter > 4:
        minE = newErr
        minWs = madeWeights
        minTester = i
        minEList = EList
        foofighters = iNodes
        if counter % 1 == 0:
            counter += 1
            print(minE)
        counter1 = 0
        if newErr < .01 and counter1 % 50 == 0:
            counter1 += 1
            print('Error List: ', minEList)
            print('layer cts: [{}, 2, 1, 1]'.format(len(tree[0])))
            for layer in madeWeights:
                print(layer)

        if newErr < .009:
            print('Error List: ', minEList)
            print('layer cts: [{}, 2, 1, 1]'.format(len(tree[0])))
            for layer in madeWeights:
                print(layer)
            quit()

print('Error List:', minE)
print('Layer Counts: [{}, 2, 1, 1]'.format(len(tree[0])))
for layer in minWs:
    print(layer)

# Pooja Somayajula, 4, 2024
