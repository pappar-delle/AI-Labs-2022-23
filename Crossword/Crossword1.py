import sys; args = sys.argv[1:]

height, width, numBS = 0, 0, 0
hWords, vWords = [], []

alphabet = 'abcdefghijklmnopqrstuvwyz#'

for i in range(len(args)):
    if '.txt' in args[i].lower():
        continue
    elif args[i][0].lower() == 'h' or args[i][0].lower() == 'v':
        k = [j for j in range(1, len(args[i])) if args[i][j].lower() in alphabet]
        if k:
            k = k[0]
            starter = args[i][1:k]
        else:
            k = 0
            starter = args[i][1:]

        vVals = int(starter[:starter.lower().find('x')])
        hVals = int(starter[starter.lower().find('x') + 1:])
        if k > 0:
            word = args[i][k:]
        if k == 0:
            word = "#"
        if args[i][0].lower() == 'h':
            hWords.append((vVals, hVals, word))
        if args[i][0].lower() == 'v':
            vWords.append((vVals, hVals, word))
    elif "x" in args[i]:
        arg = args[i]
        height = int(arg[:arg.lower().find('x')])
        width = int(arg[arg.lower().find('x') + 1:])
    elif args[i][0] in '1234567890':
        numBS = int(args[i])

default = ''.join(['-' for i in range(height*width)])
area = height * width
puzzIndexes = [[(row * width) + v for v in range(width)] for row in range(height)] + [[col + (width * n) for n in range(height)] for col in range(width)]

def printboard(puzzle, width):
    for ind in range(len(puzzle)):
        if ind % width == 0:
            print('{}'.format(puzzle[ind]), end='')
        elif ind % width == width - 1:
            print('{}\n'.format(puzzle[ind]), end='')
        else:
            print('{}'.format(puzzle[ind]), end='')
    print('\n')


def addVertical(board, vVals, hVals, word, width):
    if board == "": return ""
    wordIndexes = []
    for k in range(len(word)):
        index = (vVals + k)*width + hVals
        if index > len(board)-1:
            return ""
        wordIndexes.append(index)
    newboard = board
    for k in range(len(wordIndexes)):
        if board[wordIndexes[k]] not in ('-', '#'):
            if board[wordIndexes[k]].lower() == word[k].lower():
                continue
            else:
                return ""
        newboard = newboard[:wordIndexes[k]] + word[k] + newboard[wordIndexes[k]+1:]
    return newboard


def addHorizontal(board, vVals, hVals, word, width):
    if board == "": return ""
    startInd = vVals*width + hVals
    endInd = startInd + len(word)
    if startInd//width != (endInd-1)//width:
        return ""
    newboard = board[:startInd] + word + board[endInd:]
    return newboard


def setIndex(board, ind, char):
    if board == "":
        return board
    if board[ind] == char:
        return board
    if board[ind] in ('#'):
        return ""
    return board[:ind] + char + board[ind + 1:]


def insertWords(mat, width, hWords, vWords):
    for hWord in hWords:
        vVals, hVals, word = hWord
        mat = addHorizontal(mat, vVals, hVals, word, width)
    for vWord in vWords:
        vVals, hVals, word = vWord
        mat = addVertical(mat, vVals, hVals, word, width)
    return mat


def makeSymm(board):
    length = len(board)
    for index in range(length):
        if board[index] == '-' and board[length - 1 - index] == '#':
            board = setIndex(board, index, '#')
        elif board[index] == '#' and board[length - 1 - index] == 'L':
            return ""
    return board

# assembling

def validify(board):
    for lim in puzzIndexes:
        inds = set()
        counter = 0
        for conts in lim:
            char = board[conts]
            if char == "#":
                if counter == 2 or counter == 1:
                    for ind in inds:
                        if board[ind] != "-" or board[area - 1 - ind] != "-":
                            if board[ind] != "#" or board[area - 1 - ind] != "#": return ""
                        board[ind] = "#"
                        board[area - 1 - ind] = "#"
                counter = 0
                inds = set()
            elif lim[-1] == conts:
                if (counter == 0 or counter == 1):
                    for ind in inds:
                        if board[ind] != "-" or board[area - 1 - ind] != "-": return ""
                        board[ind] = "#"
                        board[area - 1 - ind] = "#"
            else:
                inds.add(conts)
                counter += 1
    return "".join(board)

def fillMultConnect(board, ind, ch):
    if board[ind] == "#": return board
    if ch == 1:
        if board[ind] != "-" or board[area - 1 - ind] != "-": return ""
        if ind > area - 1 - ind:
            board = board[:area - 1 - ind] + "#" + board[area - ind:ind] + "#" + board[ind + 1:]
        elif ind < area - 1 - ind:
            board = board[:ind] + "#" + board[ind + 1:area - 1 - ind] + "#" + board[area - ind:]
        else:
            board = board[:ind] + "#" + board[ind + 1:]
        if ind % width != 0:
            board = fillMultConnect(board, ind - 1, 1)
            if not board: return ""
        if ind + width < area:
            board = fillMultConnect(board, ind + width, 1)
            if not board: return ""
        if ind - width > 0:
            board = fillMultConnect(board, ind - width, 1)
            if not board: return ""
        if (ind % width) != (width - 1):
            board = fillMultConnect(board, ind + 1, 1)
            if not board: return ""
    if ch == 2:
        board = board[:ind] + "#" + board[ind + 1:]
        if ind - width > 0:
            board = fillMultConnect(board, ind - width, 2)
        if ind + width < area:
            board = fillMultConnect(board, ind + width, 2)
        if ind % width != 0:
            board = fillMultConnect(board, ind - 1, 2)
        if ind % width != width - 1:
            board = fillMultConnect(board, ind + 1, 2)
    return board

def checkConnect(board):
    index = board.find("-")
    if index == -1:
        return False
    newboard = fillMultConnect(board, index, 2)
    return any([True for ch in newboard if ch != "#"])

def connect4(board, numBlocks):
    newboard = ""
    while checkConnect(board):
        for index in range(area):
            if board[index] == "-":
                newboard = fillMultConnect(board, index, 1)
                if not newboard or newboard.count("#") > numBlocks: continue
                else:
                    break
        board = newboard
    return board

def findSpace(board):
    empty = set()
    indLims = (area // 2) if area % 2 == 0 else ((area // 2) + 1)
    for ind in range(indLims):
        if board[ind] == "-" and board[area - 1 - ind] == "-":
            empty.add(ind)
    return empty

def assembleRecur(board, numBlocks):
    if board != "":
        newboard = validify([*board])
        if not newboard:
            return ""
        presBlock = newboard.count("#")
        if presBlock > numBlocks:
            return ""
        while newboard != board:
            board = newboard
            newboard = validify([*newboard])
            if not newboard:
                return ""
            presBlock = newboard.count("#")
            if presBlock > numBlocks:
                return ""
        if checkConnect(board):
            return ""
        if presBlock == numBlocks: return board
    for ind in findSpace(board):
        if ind > area - 1 - ind:
            ab = board[:area - 1 - ind] + "#" + board[area - ind:ind] + "#" + board[ind + 1:]
        elif ind < area - 1 - ind:
            ab = board[:ind] + "#" + board[ind + 1:area - 1 - ind] + "#" + board[area - ind:]
        else:
            ab = board[:ind] + "#" + board[ind + 1:]
        nB = assembleRecur(ab, numBlocks)
        if nB:
            return nB
    return ""

def main():
    board = insertWords(default, width, hWords, vWords)
    board = validify([*makeSymm(board)])
    board = connect4(board, numBS)
    board = assembleRecur(board, numBS)
    printboard(board, width)

if __name__ == '__main__':
    main()

# Pooja Somayajula, 4, 2024
