import sys; args = sys.argv[1:]

def switchTok(token):
    return 'X' if token == 'O' else 'O'

default = '.'*27 + 'OX......XO' + '.'*27
nbrs = {}


indexList = []
futMoveCache = {}
cbCache = {}
holeLim = 0
movesCache = {}
makeMoveCache = {}
moveSeqCache = {}


moveBoard = {index: {key for key in indexList[index]} for index in nbrs}
getRid = {key for key in moveBoard if len(moveBoard[key]) == 0}
for i in getRid:
    del moveBoard[i]
oTok = {'X':'O', 'O':'X'}
CNR_EDGES = {0: {1,2,3,4,5,6,7,8,16,24,32,40,48,56},
             7: {0,1,2,3,4,5,6,15,23,31,39,47,55,63},
             56: {0,8,16,24,32,40,48,57,58,59,60,61,62,63},
             63: {7,15,23,31,39,47,55,56,57,58,59,60,61,62}}
EDGE_CNR = {edgeInd: corner for corner in CNR_EDGES for edgeInd in CNR_EDGES[corner]}

def printBoard(board, possMoves):
    print("\n".join(["".join([board[i] if i not in possMoves else "*" for i in range(ind, ind+8)]) for ind in range(0, len(board), 8)]) + "\n")

n = "0123456789"
TOKS = ".oOXx"
dot = "."

cnr = [0, 7, 56, 63]
CORNERS = {0, 7, 56, 63}
cnrNeigh = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}

top = [i for i in range(8)]
bottom = [(56) + i for i in range(8)]

left = [(8 * i) for i in range(8)]
right = [7 + (8 * i) for i in range(8)]

edgeList = bottom + top + left + right

indexes = []
for r in range(0, 8):
    indexes.append([(r * 8) + v for v in range(8)])

for c in range(0, 8):
    indexes.append([c + (8 * n) for n in range(8)])

for j in range(8 - 2):
    indexes.append([(j + i * (8 + 1)) for i in range(8 - j)])

for j in range(8, 64 - 8 * 2, 8):
    indexes.append([(j + i * (8 + 1)) for i in range(8 - (j // 8))])

for j in range(2, 8):
    indexes.append([(j + i * (8 - 1)) for i in range(0, j + 1)])

for j in range(8 * 2 - 1, 64 - 8 * 2, 8):
    indexes.append([(j + i * (8 - 1)) for i in range(8 - (j // 8))])

indConts = {i: [indexSet for indexSet in indexes if i in indexSet] for i in range(0, 64)}

indexToks = {'O': {i for i in range(64) if default[i] == 'O'} - {0, 7, 56, 63}, 'X': {i for i in range(64) if default[i] == 'X'} - {0, 7, 56, 63}}


def main():
    board = ""
    token = ""
    default = '.' * 27 + 'OX......XO' + '.' * 27
    holeLim = 0
    listMoves = []
    for i in range(len(args)):
        if not args[i]:continue
        elif len(args[i]) >= 3 and args[i][:2] == 'HL':
            holeLim = int(args[i][2:])
        elif len(args[i]) == 64 and args[i][0] in TOKS:
            board = args[i].upper()
        elif args[i].upper() in TOKS: token = args[i].upper()
        else:
            listMoves = condensedPath(listMoves, args[i])
    if not board:
        board = default
    if not token:
        token = switch(board)
    moveSet = findMoves(board, token)
    if not moveSet:
        token = switchTok(token)
        moveSet = findMoves(board, token)
    global startboard, startTok
    startboard = board
    startTok = token

    if not listMoves:
        printBoard(board, moveSet)
        print(board + " " + str(board.count("X")) + "/" + str(board.count("O")))
        print("Possible moves for " + token + ": " + ", ".join([str(ch) for ch in moveSet]) + "\n")

    for i in listMoves:
        if i >= 0:
            print(token + " moves to " + str(i))
            board = makeMove(board, token, i)
            Ihatethegrader = board[:i] + token.lower() + board[i+1:]

            token = switchTok(token)
            moveSet = findMoves(board, token)
            if not moveSet:
                token = switchTok(token)
                moveSet = findMoves(board, token)
            printBoard(Ihatethegrader, moveSet)
            print(Ihatethegrader + " " + str(board.count("X")) + "/" + str(board.count("O")))
            if moveSet:
                print("Possible moves for " + token + ": " + ", ".join([str(ch) for ch in moveSet]) + "\n")
            else:
                print("No Moves Possible")
                break
    movesLeft = board.count('.')
    if movesLeft > 0 and len(moveSet) > 0:
        print("Preferred Move: ", movePref(moveSet, board, token))
        if movesLeft < holeLim:
            ab = alphabetaMain(board, token, -65, 65)


def condensedPath(listMoves, movePath):
    if len(movePath) == 1:
        listMoves.append(int(movePath))
        return listMoves
    moveList = [movePath[i:i+2] for i in range(0, len(movePath), 2)]
    for play in moveList:
        if play[0] == "_":
            listMoves.append(int(play[1]))
            continue
        if play[0] == "-" or play[0] in n:
            listMoves.append(int(play))
            continue
        if play[0].upper() in 'ABCDEFGH':
            col = 'ABCDEFGH'.index(play[0].upper())
            listMoves.append(col+ (int(play[1])-1)*8)
    return listMoves

def findMoves(board, token):
    moveSet = set()
    for i in range(len(board)):
        if board[i] != token:
            continue
        for boardLookUp in indConts[i]:
            pIND = ""
            hasSeenOp = False
            hasSeenTok = False

            for j in boardLookUp:
                if board[j] == ".":
                    pIND = j
                    if not hasSeenTok:
                        hasSeenOp = False
                    elif hasSeenOp:
                        moveSet.add(j)
                        break
                    else:
                        break

                elif board[j] == token:
                    if j == i:
                        hasSeenTok = True
                        if hasSeenOp and pIND != "":
                            moveSet.add(pIND)
                    hasSeenOp = False
                    pIND = ""
                else: hasSeenOp = True
    return moveSet


def flipThemBoyz(board, token, indList, switchToks):
    ind = 0
    possFlips = set()
    while board[indList[ind]] != token and board[indList[ind]] != dot:
        possFlips.add(indList[ind])
        ind += 1
        if ind >= len(indList):
            return switchToks
    if board[indList[ind]] == token:
        switchToks.update(possFlips)
    return switchToks



def setitems(mv, cL):
    place = cL.index(mv)
    return place, cL[:place][::-1], cL[place + 1:]

def makeMove(board, token, move):
    tokensToSwitch = {move}
    for boardLookUp in indConts[move]:
        movePlacement, prevInd , forInd = setitems(move, boardLookUp)
        if forInd and len(forInd) > 1:
            tokensToSwitch = flipThemBoyz(board, token, forInd, tokensToSwitch)
        if prevInd and len(prevInd) > 1:
            tokensToSwitch = flipThemBoyz(board, token, prevInd, tokensToSwitch)
    return "".join([board[i] if i not in tokensToSwitch else token for i in range(64)])


def edgeSearch(spot_1, spot_2, openSpot, edges, move, board, token):
    edgeTok = switchTok(token)
    edgeTokPoss = False
    ind = move + openSpot
    if board[ind] == edgeTok:
        edgeTokPoss = True
    if board[spot_2] == token:
        while ind != spot_2:
            if board[ind] == dot or (board[ind] == edgeTok and not edgeTokPoss):
                break
            if board[ind] == token and edgeTokPoss:
                edgeTokPoss = False
            ind += openSpot
        if ind == spot_2:
            edges.add(move)
    edgeTokPoss = False
    ind = move - openSpot
    if board[ind] == edgeTok: edgeTokPoss = True
    if board[spot_1] == token:
        while ind != spot_1:
            if board[ind] == dot or (board[ind] == edgeTok and not edgeTokPoss):
                break
            if board[ind] == token and edgeTokPoss: edgeTokPoss = False
            ind = ind - openSpot
        if ind == spot_1: edges.add(move)
    return edges



def countToks(board, edge, token):
    counter = 0
    for i in edge:
        if board[i] == token:
            counter +=1
    return counter



def playBall(possMoveSet, board, token):
    edgeTok = switchTok(token)
    failed = []
    passed = []
    for move in possMoveSet:
        if any([True for m in findMoves(makeMove(board, token, move), edgeTok) if m in cnr]):
            failed.append(move)
        else:
            passed.append(move)
    if passed:
        return passed[0]
    return failed[0]

def switch(board):
    if board.count('.') % 2 == 0:
        return 'X'
    return 'O'

def movePref(possMoveSet, board, token):
    possEdge = set()
    edgeSet = set()
    prospects = set()

    for move in possMoveSet:
        if move in cnr:
            return move
    for i in possMoveSet:
        prospects.add(i)

    for i in possMoveSet:
        pick = True
        if i in cnrNeigh:
            if board[cnrNeigh[i]] != token:
                prospects.remove(i)
                pick = False
        if i in edgeList:

            if i in left:
                possEdge = edgeSearch(0, 56, 8, possEdge, i, board, token)
                if countToks(board, left, dot) == 1: possEdge.add(i)

            elif i in top:
                possEdge = edgeSearch(0, 7, 1, possEdge, i, board, token)
                if countToks(board, top, dot) == 1: possEdge.add(i)

            elif i in right:
                possEdge = edgeSearch(7, 63, 8, possEdge, i, board, token)
                if countToks(board, right, dot) == 1: possEdge.add(i)

            elif i in bottom:
                possEdge = edgeSearch(56, 63, 1, possEdge, i, board, token)
                if countToks(board, bottom, dot) == 1: possEdge.add(i)

            if pick: edgeSet.add(i)

    if possEdge:
        keepTrack = {}
        for m in possEdge:
            newBoard = makeMove(board, token, m)
            if m in top:
                keepTrack[countToks(newBoard, top, token)] = m
            elif m in bottom:
                keepTrack[countToks(newBoard, bottom, token)] = m
            elif m in left:
                keepTrack[countToks(newBoard, left, token)] = m
            else:
                keepTrack[countToks(newBoard, right, token)] = m
        ind = max(keepTrack)
        return keepTrack[ind]

    if prospects: return playBall(prospects, board, token)
    return playBall(possMoveSet, board, token)

def quickMove(board, token):
    if not board:
        global holeLim
        holeLim = token
    else:
        board = board.upper()
        token = token.upper()
        possMoveSet = findMoves(board, token)
        numHoles = board.count('.')
        if numHoles < holeLim:
            ab = alphabetaMain(board, token, -65, 65)
            return ab[-1]
        return movePref(possMoveSet, board, token)


#Othello6
def alphabeta(board, token, lwrBnd, uprBnd):
    cnrMoves = []
    futMoves = []
    opptoken = opptokens[token]
    if (board, token) not in movesCache:
        movesCache[(board, token)] = findMoves(board, token)
    possibloppMoves = movesCache[(board, token)]
    if not possibloppMoves:
        if (board, opptoken) not in movesCache:
            movesCache[(board, opptoken)] = findMoves(board, opptoken)
        oppMoves = movesCache[(board, opptoken)]
        if not oppMoves: return [board.count(token) - board.count(opptoken)]
        ab = alphabeta(board, opptoken, -uprBnd, -lwrBnd)
        return [-ab[0]] + ab[1:] + [-1]
    best = [lwrBnd-1]

    for move in possibloppMoves:
        if move in CORNERS:
            cnrMoves.append(move)
        else:
            futMoves.append(move)
    cnrMoves.extend(futMoves)

    moves = cnrMoves
    for move in moves:
        if (board, token, move) not in makeMoveCache:
            makeMoveCache[(board, token, move)] = makeMove(board, token, move)
        newboard = makeMoveCache[(board, token, move)]
        ab = alphabeta(newboard, opptoken, -uprBnd, -lwrBnd)
        score = -ab[0]
        if score < lwrBnd: continue
        if score > uprBnd: return [score]
        best = [score] + ab[1:] + [move]
        lwrBnd = score + 1
    return best

opptokens = {'X':'O', 'O':'X'}

def alphabetaMain(board, token, lwrBnd, uprBnd):
    cnrMoves = []
    futMoves = []
    opptoken = opptokens[token]
    if (board, token) not in movesCache:
        movesCache[(board, token)] = findMoves(board, token)
    possibloppMoves = movesCache[(board, token)]
    if not possibloppMoves:
        if (board, opptoken) not in movesCache:
            movesCache[(board, opptoken)] = findMoves(board, opptoken)
        oppMoves = movesCache[(board, opptoken)]
        if not oppMoves: return [board.count(token) - board.count(opptoken)]
        ab = alphabeta(board, opptoken, -uprBnd, -lwrBnd)
        return [-ab[0]] + ab[1:] + [-1]
    best = [lwrBnd-1]

    for move in possibloppMoves:
        if move in CORNERS:
            cnrMoves.append(move)
        else:
            futMoves.append(move)
    cnrMoves.extend(futMoves)

    moves = cnrMoves
    for mv in moves:
        if (board, token, mv) not in makeMoveCache:
            makeMoveCache[(board, token, mv)] = makeMove(board, token, mv)
        newboard = makeMoveCache[(board, token, mv)]
        ab = alphabeta(newboard, opptoken, -uprBnd, -lwrBnd)
        score = -ab[0]
        if score < lwrBnd: continue
        if score > uprBnd: return [score]
        best = [score] + ab[1:] + [mv]
        lwrBnd = score + 1
        print(f"Score: {score}; Sequence: {best[1:]}")
    return best



if __name__ == "__main__":
    main()

# Pooja Somayajula, 4, 2024
