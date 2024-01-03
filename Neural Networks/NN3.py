import sys; args = sys.argv[1:]
import math, random

inEq = args[0]
inputs = []
trainingValues = []

i = 7
ineqOp = inEq[i]
i += 1
if inEq[i] == '=':
    ineqOp += inEq[i]
    i += 1
#print(inEq)
#print(i)
cir_r2 = float(inEq[i:])
#print(ineqOp)
#print(cir_r2)

def setTrainingValues(r2, ineqOp, count1, count2):
    cir_r = math.sqrt(r2)

    radius_cnt = count1
    angle_cnt = count2
    inputs = []
    trainingValues = []

    # Create training values inside the circle
    if ineqOp in ["<", "<="]:  ## valid values are all inside the circle
        result = 1
    else:  ## valid values are all outside the circle
        result = 0
    inputs.append([0, 0, 1])
    trainingValues.append([result])
    for ri in range(1, radius_cnt):
        r = ri * cir_r / radius_cnt
        for ai in range(1, angle_cnt):
            a = ai * math.pi / 4 / angle_cnt
            x = r * math.cos(a)
            y = r * math.sin(a)
            inputs.append([x, y, 1])
            trainingValues.append([result])
            inputs.append([-x, y, 1])
            trainingValues.append([result])
            inputs.append([-x, -y, 1])
            trainingValues.append([result])
            inputs.append([x, -y, 1])
            trainingValues.append([result])

    # Create training values outside the circle
    vmax = 1.5
    result = [1, 0][result]
    for ri in range(1, radius_cnt):
        r = cir_r + ri * (vmax - cir_r) / radius_cnt
        for ai in range(1, angle_cnt):
            a = ai * math.pi / 4 / angle_cnt
            x = r * math.cos(a)
            y = r * math.sin(a)
            inputs.append([x, y, 1])
            trainingValues.append([result])
            inputs.append([-x, y, 1])
            trainingValues.append([result])
            inputs.append([-x, -y, 1])
            trainingValues.append([result])
            inputs.append([x, -y, 1])
            trainingValues.append([result])
    inputs.append([vmax, 0, 1])
    trainingValues.append([result])
    inputs.append([vmax, vmax, 1])
    trainingValues.append([result])
    inputs.append([vmax, -vmax, 1])
    trainingValues.append([result])
    inputs.append([0, vmax, 1])
    trainingValues.append([result])
    inputs.append([0, -vmax, 1])
    trainingValues.append([result])
    inputs.append([-vmax, 0, 1])
    trainingValues.append([result])
    inputs.append([-vmax, vmax, 1])
    trainingValues.append([result])
    inputs.append([-vmax, -vmax, 1])
    trainingValues.append([result])

    # Create training values on the circle
    if ineqOp in ["<=", ">="]:  ## points on the circle are valid values
        result = 1
    else:  ## points on the circle are not valid values
        result = 0
    for ai in range(0, angle_cnt):
        a = ai * math.pi / 4 / angle_cnt
        x = cir_r * math.cos(a)
        y = cir_r * math.sin(a)
        inputs.append([x, y, 1])
        trainingValues.append([result])
        inputs.append([-x, y, 1])
        trainingValues.append([result])
        inputs.append([-x, -y, 1])
        trainingValues.append([result])
        inputs.append([x, -y, 1])
        trainingValues.append([result])

    inputCount = 3
    outputCount = 1

    return inputs, trainingValues, inputCount, outputCount

def sortTrainingValues(inputs, trainingValues):
    temp = [(random.random(), i) for i in range(len(inputs))]
    temp.sort()
    inputs2 = []
    trainingValues2 = []
    for i in range(len(temp)):
        inputs2.append(inputs[temp[i][1]])
        trainingValues2.append(trainingValues[temp[i][1]])
    #return inputs2, trainingValues2

    splitPoint = len(temp) * 2 // 3
    return inputs2[:splitPoint], trainingValues2[:splitPoint], inputs2[splitPoint:], trainingValues2[splitPoint:]

def initializeWeights(inputCnt, outputCnt):
    #weights = [[0] * [(inputCnt)*2, (outputCnt+1)*2, (outputCnt+1)*outputCnt, outputCnt][i] for i in range(4)]
    nodeCounts = [inputCnt, 2, outputCnt+1, outputCnt, 1]  # last entry is dummy
    weightCounts = [nodeCounts[i]*nodeCounts[i+1] for i in range(len(nodeCounts)-1)]
    weights = [[0] * weightCounts[j] for j in range(len(weightCounts))]

    for j in range(len(weights)):
        for k in range(len(weights[j])):
            weights[j][k] = random.random()
    return weights

def dotproduct(a, b):
    product = 0
    for i in range(len(a)):
        product += a[i]*b[i]
    return product

def HadamondProduct(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c

def transferFunction(input): # logarithmic function 1/(1+e^-x)
    e = math.exp(-1*input)
    ans = 1/(1+e)
    return ans

def feedForwardNetwork(nodes, weights):
    for idx, layer in enumerate(weights):
        if idx == len(weights)-1:
            for i, node in enumerate(nodes[idx]):
                nodes[idx+1].append(node*layer[i])
        else:
            numOutputNodes = int(len(layer)/len(nodes[idx])+0.5)
            j = 0
            for newNode in range(numOutputNodes):
                newN = 0
                for node in nodes[idx]:
                    newN += node*layer[j]
                    j += 1
                newN = transferFunction(newN)
                nodes[idx+1].append(newN)
    return nodes

def backPropagationNetwork(weights, inputs, expected, inputCnt, outputCnt):
    c = 0.1
    numTrials = 100000
    for cnt in range(numTrials):
        nodes = [[] for i in range(len(weights) + 1)]
        numInput = cnt % len(inputs)
        nodes[0] = inputs[numInput]
        nodes = feedForwardNetwork(nodes, weights)
        eVals = backPropagation(nodes, weights, expected[numInput], inputCnt, outputCnt)
        for lidx, layer in enumerate(weights):
            nodeCount = len(nodes[lidx])
            for widx, weight in enumerate(layer):
                if layer == weights[-1]:
                    weights[lidx][widx] += c * nodes[lidx][widx] * eVals[lidx + 1][widx]
                else:
                    weights[lidx][widx] += c * nodes[lidx][widx % nodeCount] * eVals[lidx + 1][widx // nodeCount]

                #weights[lidx][widx] += c * nodes[lidx][widx % nodeCount] * eVals[lidx+1][widx // nodeCount]

        #if cnt % 10000 == 0:
            #print("Layer counts " + str(inputCount) + " 2 " + str(outputCount + 1) + " " + str(outputCount) + " " + str(outputCount))
            #for i in range(len(weights)):
                #print(weights[i])
        if cnt == numTrials//2:
            if calcError(weights, inputs, expected) > 1.5:
                return weights
    return weights

def backPropagation(nodes, weights, expected, inputCnt, outputCnt):
    eVals = [[0] * [1, 2, outputCnt+1, outputCnt, outputCnt][j] for j in range(5)]

    eVals[-1] = [expected[i] - nodes[-1][i] for i in range(len(expected))]

    lidx = len(eVals)-2
    for nidx in range(len(eVals[-2])):
        x = nodes[lidx][nidx]
        sumE = weights[lidx][nidx]*eVals[lidx+1][nidx]
        par = x*(1-x)*sumE
        eVals[lidx][nidx] = par

    for lidx in range(len(eVals)-3, 0, -1):
        for nidx in range(len(eVals[lidx])):
            x = nodes[lidx][nidx]
            sumE = 0
            nodeCnt = len(nodes[lidx])
            for i in range(len(weights[lidx])):
                if i % nodeCnt == nidx:
                    sumE += weights[lidx][i] * eVals[lidx+1][i//nodeCnt]
            par = x*(1-x)*sumE
            eVals[lidx][nidx] = par
    return eVals

def calcError(weights, inputs, trainingValues):
    errorSum = 0
    for i, inp in enumerate(inputs):
        nodes = [[] for n in range(len(weights) + 1)]
        nodes[0] = inp
        nodes = feedForwardNetwork(nodes, weights)
        for j in range(len(trainingValues[i])):
            errorSum += (trainingValues[i][j] - nodes[-1][j])**2
    return errorSum / 2

def createNetwork(inputs, trainingValues, inputCount, outputCount):
    weights = initializeWeights(inputCount, outputCount)
    weights = backPropagationNetwork(weights, inputs, trainingValues, inputCount, outputCount)
    return weights

all_inputs, all_trainingValues, inputCount, outputCount = setTrainingValues(cir_r2, ineqOp, 4, 3)
#inputs, trainingValues, tst_inputs, tst_trainingValues = sortTrainingValues(all_inputs, all_trainingValues)
weights = initializeWeights(inputCount, outputCount)

# maintain a counter, best weights (lowest error so far)
# if it passed 10, come out and print best weights
#best_error = calcError(weights, inputs, trainingValues)
best_error = 1000000
best_weights = [[*weight] for weight in weights]
num_tries = 0
while num_tries < 40:
    inputs, trainingValues, tst_inputs, tst_trainingValues = sortTrainingValues(all_inputs, all_trainingValues)
    weights = createNetwork(inputs, trainingValues, inputCount, outputCount)
    err = calcError(weights, tst_inputs, tst_trainingValues)
    if err < best_error:
        best_error = err
        best_weights = [[*weight] for weight in weights]
        #print("Error: " + str(best_error))
        print("Layer counts " + str(inputCount) + " 2 " + str(outputCount+1) + " " + str(outputCount) + " " + str(outputCount))
        for i in range(len(weights)):
            print(weights[i])
    if err <= 0.01:
        break
    num_tries += 1

#print("Error: " + str(best_error))
print("Layer counts " + str(inputCount) + " 2 " + str(outputCount+1) + " " + str(outputCount) + " " + str(outputCount))
for i in range(len(best_weights)):
    print(best_weights[i])

# test weights
#print(); print("Testing:")
#t_inputs, t_trainingValues, t1, t2 = setTrainingValues(cir_r2, ineqOp, 4, 4)
#for i, inp in enumerate(all_inputs):
#    nodes = [[] for n in range(len(best_weights) + 1)]
#    nodes[0] = inp
#    nodes = feedForwardNetwork(nodes, best_weights)
#    print(str(inp) + "->" + str(all_trainingValues[i][0]) + ": " + str(nodes[-1][0]) + ", " + str(all_trainingValues[i][0] - nodes[-1][0]))
# Raka Adakroy, 7, 2024
