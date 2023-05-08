import sys; args = sys.argv[1:]
import math

txtFile, func, inpts = args[0], args[1], [float(k) for k in args[2:]]
with open(args[0]) as wFile:
    wList = []
    for line in wFile:
        wList.append([float(i) for i in line.strip().split(' ')])

def calculateNodes(inputs, weightLine):
    global func
    inpNums = len(inputs)
    inpCells = int(len(weightLine)/inpNums)
    indList = []
    for i in range(0, inpCells):
        indList.append(weightLine[i * inpNums: i * inpNums + inpNums])
    nodeList = []
    for i in indList:
        val = dotProduct(inputs, i)
        if func == 'T1':
           nodeList.append(val)
        elif func == 'T2':
            if val > 0:
                nodeList.append(val)
            else:
                nodeList.append(0)
        elif func == 'T3':
            nodeList.append(1 / (1 + math.exp(-val)))
        elif func == 'T4':
            nodeList.append(-1 + (2 / (1 + math.exp(-val))))
    return nodeList


def dotProduct(vector1, vector2):
    productList = []
    for i in range(0, len(vector1)):
        productList.append(vector1[i] * vector2[i])
    return sum(productList)


def feedForward(inpts, wList):
    inputs = inpts
    tree = []
    for depth in range(0, len(wList)-1):
        tree.append(inputs)
        inputs = calculateNodes(inputs, wList[depth])
    resultList = [inputs[i] * wList[len(wList)-1][i] for i in range(0, len(inputs))]
    tree.append(resultList)
    print(tree)
    return resultList

def main():
    print(' '.join(str(i) for i in feedForward(inpts, wList)))


if __name__ == '__main__': main()


# Pooja Somayajula, 4, 2024
