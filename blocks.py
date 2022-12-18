import sys;args = sys.argv[1:]
import time

# see if total area is less than block area, if not continue

def main():
    start = time.time()
    structureBlocks = ' '.join(args[0:]).replace('x', ' ').replace("X", " ")
    structureBlocks = structureBlocks.split(" ")

    # essentially a set globals routine
    global bHeight, bWidth, blocks, totalArea, blockArea, template, debugging, bigDeb
    bHeight, bWidth = int(structureBlocks[0]), int(structureBlocks[1])
    blocks = {}
    for i in range(2, len(structureBlocks), 2):
        blocks[int(i / 2)] = (structureBlocks[i], structureBlocks[i + 1])
    totalArea = bWidth * bHeight
    blockArea = 0
    for i in blocks:
        blockArea += int(blocks[i][0]) * int(blocks[i][1])


    # add extra 'filler' blocks
    if blockArea < totalArea:
        starting = len(blocks) + 1
        for i in range(totalArea - blockArea):
            blocks[starting] = ('1', '1')
            starting += 1
    template = {j: ''.join(['.' for i in range(bWidth)]) for j in range(bHeight)}
    debugging = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    bigDeb = {key: debugging[key] for key in blocks}

    if totalArea >= blockArea:
        print(printDecomp(bruteForce(template, 0, bigDeb)))
        print(time.time()-start)
    else:
        print(printDecomp(False))


def isPossible(blockInd, pos, temp, h, w):
    i, j = pos
    keepTrack = bigDeb[blockInd]

    if fitsIn(pos, temp, w, h):
        copyTemp = dict(temp)
        for changeUp in range(j, j + h):
            copyTemp[changeUp] = temp[changeUp][:i] + (keepTrack * w) + temp[changeUp][i + w:]
        return copyTemp

    return False

def printDecomp(temp):
    if temp == False:
        return 'No solution'
    decomp = []
    blockOps = {bigDeb[i] : i for i in bigDeb}

    checked = set()
    for row in temp:
        for i in range(len(temp[row])):
            newRow = temp[row]
            keyVal = newRow[i]
            if keyVal in checked: continue
            checked.add(keyVal)
            h, w, = blocks[int(blockOps[keyVal])]
            doesE = newRow.rfind(keyVal)
            decomp.append('{}x{}'.format(h, w)) if i + int(w) - 1 == doesE else decomp.append('{}x{}'.format(w, h))

    bigBoy = "Decomposition: "
    for key in decomp:  bigBoy += key + " "
    bigBoy.strip()
    return bigBoy

def fitsIn(upp, temp, w, h):
    i, j = upp
    if (i + w) > bWidth:
        return False
    elif temp[j][i:i + w].count('.') < w:
        return False
    elif (j + h) > bHeight:
        return False
    return True

#recursive
def bruteForce(temp, currentRow, debug):
    if '.' not in temp[bHeight - 1]: return temp
    if '.' in temp[currentRow]: nextPos = temp[currentRow].find('.')
    else:
        while '.' not in temp[currentRow]: currentRow += 1
        nextPos = temp[currentRow].find('.')
    for itm in debug:
        h, w = int(blocks[itm][0]), int(blocks[itm][1])
        choiceCop = dict(debug)
        choiceCop.pop(itm)
        for i in range(0,2):
            if i == 0:
                currentTemp = isPossible(itm, (nextPos, currentRow), temp, h, w)
                if currentTemp:
                    result = bruteForce(currentTemp, currentRow, choiceCop)
                    if result:return result
            if h != w:
                if i == 1:
                    w, h = int(blocks[itm][0]), int(blocks[itm][1])
                    currentTemp = isPossible(itm, (nextPos, currentRow), temp, h, w)
                    if currentTemp:
                        result = bruteForce(currentTemp, currentRow, choiceCop)
                        if result:return result
    return False

if __name__ == '__main__':main()

# Pooja Somayajula, 4, 2024
