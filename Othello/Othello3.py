import sys;args = sys.argv[1:]

default = '.'*27 + 'ox......xo' + '.'*27
startTok = ''
listMoves = []

for i in range(0, len(args)):
    if len(args[i]) == 64:
        default = args[i].lower()
    elif len(args[i]) in (1, 2):
        if args[i].lower() in 'xo':
            startTok = args[i].lower()
        elif args[i][0].lower() in 'abcdefgh':
            listMoves.append((int(args[i][1])-1)*8 + 'abcdefgh'.index(args[i][0].lower()))
        else:
            listMoves.append(int(args[i]))
    else:
        print('Wrong inputs at index {}:\nlength {}, {}'.format(i, len(args[i]), args[i]))

indexToks = {'o': {i for i in range(64) if default[i] == 'o'} - {0, 7, 56, 63}, 'x': {i for i in range(64) if default[i] == 'x'} - {0, 7, 56, 63}}
nbrs = {}
newp = [i for i in range(0, len(default))]

CNR_EDGES = {0: {1,2,3,4,5,6,7,8,16,24,32,40,48,56}, 7: {0,1,2,3,4,5,6,15,23,31,39,47,55,63},
         56: {0,8,16,24,32,40,48,57,58,59,60,61,62,63}, 63: {7,15,23,31,39,47,55,56,57,58,59,60,61,62}}
EDGE_CNR = {edgeInd: corner for corner in CNR_EDGES for edgeInd in CNR_EDGES[corner]}
CORNERS = {0, 7, 56, 63}
CX = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}

for i in newp:
    if i % 8 == 0:
        nbrs[i] = {i + 1,i - 8, i + 8,i - 7,i + 9}.intersection(newp)
    elif i % 8 == 7:
        nbrs[i] = {i - 1, i - 8, i + 8, i + 7, i - 9}.intersection(newp)
    else:
        nbrs[i] = {i - 1,i + 1, i - 8, i + 8, i - 7, i + 7, i - 9, i + 9}.intersection(newp)
indexList = []

for i in newp:
    indDict = {nbr: [] for nbr in nbrs[i]}
    for n in nbrs[i]:
        diff = i - n
        prev = n
        current = n + diff
        while -1 < current < 64 and current in nbrs[prev]:
            if current != i: indDict[n].append(current)
            prev = current
            current = current + diff
        if len(indDict[n]) == 0:
            del indDict[n]
    indexList.append(indDict)

moveBoard = {index: {key for key in indexList[index]} for index in nbrs}
getRid = {key for key in moveBoard if len(moveBoard[key]) == 0}
for i in getRid:
    del moveBoard[i]

def formatMoves(board, possMoves):
    askBoard = ''.join([ch if idx not in possMoves else '*' for idx, ch in enumerate(board)])
    for i in range(0, 64, 8): print(' '.join(askBoard[i:i + 8]))


def isValid(token, nextI, adI, board):
    possInds = indexList[adI][nextI]
    for i in possInds:
        if board[i] == '.':return -1
        elif board[i] == token:return i
    return -1


def countToks(board):
    return board.count('x'), board.count('o')


def switch(board):
    if board.count('.') % 2 == 0:
        return 'x', 'o'
    return 'o', 'x'


def switchTok(token):
    return 'x' if token == 'o' else 'o'

def findMoves(board, toks = ''):

    moveSet = set()
    if toks == '': token, oTok = switch(board)
    else: toks, oTok = toks, switchTok(toks)
    for i in indexToks[oTok]:
        for n in moveBoard[i]:
            if board[n] == '.':
                if isValid(toks, n, i, board) != -1:
                    moveSet.add(n)
    return len(moveSet), moveSet


def changePos(board, token, position):
    oTok = switchTok(token)
    nextOpp = {nbr for nbr in nbrs[position] if board[nbr] == oTok and position in indexList[nbr]}

    for opp in nextOpp:
        i = isValid(token, position, opp, board)
        if i > -1:
            subset = indexList[opp][position]
            changes = set(subset[:subset.index(i) + 1] + [position, opp])
            indexToks[token] = indexToks[token].union(changes) - {0, 7, 56, 63}
            indexToks[oTok] = indexToks[oTok] - changes
            board = ''.join([ch if ind not in changes else token for ind, ch in enumerate(board)])
    return board

def formatPoss(passSet):
    return ", ".join([str(i) for i in sorted(passSet)])

def playBall(currentTok, oppTok, movePos, board):
    print('\n{} plays to {}:'.format(currentTok, movePos))
    flippedBoard = changePos(board, currentTok, movePos)
    xTokens, oTokens = countToks(flippedBoard)
    canOMove, oMoves = findMoves(flippedBoard, oppTok)
    if canOMove:
        formatMoves(flippedBoard, oMoves)
        print('\n' + flippedBoard + ' {}/{}'.format(xTokens, oTokens))
        print('Possible moves for {}: {}'.format(oppTok, formatPoss(oMoves)))
        return oppTok, currentTok, flippedBoard
    else:
        canMove, possMoves = findMoves(flippedBoard, currentTok)
        formatMoves(flippedBoard, oMoves)
        print('\n' + flippedBoard + ' {}/{}'.format(xTokens, oTokens))
        if canMove:
            print('Possible moves for {}: {}'.format(currentTok, formatPoss(possMoves)))
        return currentTok, oppTok, flippedBoard


if startTok == '':
    startTok, oppTok = switch(default)
else:
    oppTok = switchTok(startTok)
canMove, possMoves = findMoves(default, startTok)
if canMove == False:
    canMove, possMoves = findMoves(default, oppTok)
    startTok, oppTok = oppTok, startTok

if len(listMoves) > 0:
    formatMoves(default, possMoves)
    canMove, possMoves = findMoves(default, startTok)
    xTok, oTok = countToks(default)
    print('\n' + default + ' {}/{}'.format(xTok, oTok))
    if canMove:
        print('Possible moves for {}: {}'.format(startTok, formatPoss(possMoves)))
    for movePos in listMoves:
        if movePos < 0: continue
        startTok, oppTok, default = playBall(startTok, oppTok, movePos, default)

elif len(listMoves) == 0:
    xTokens, oTokens = countToks(default)
    formatMoves(default, possMoves)
    print('\n' + default + ' {}/{}'.format(xTokens, oTokens))
    if canMove:
        print('Possible moves for {}: {}'.format(startTok, formatPoss(possMoves)))

# Pooja Somayajula, 4, 2024
