#Submit a script that takes up to two command line arguments, both optional.

#The first is an Othello board, represented by a string of 64 characters from {*".xoXO"}.  The default, if the board is not provided is '.'*27 + "ox......xo" + '.'*27

#The second is the token for which to find the set of moves.  The default, if not provided, is the token that would move if there had been no passes in any prior moves.

#The output is to be a 2D representation of the board, with possible move positions indicated by an asterisk.  
#Following this (on one line) should be a sequence of all possible moves, as integers, where each integer is in range(64).  
#If no moves are possible for the token in question, print out: No moves possible.  
#Note: it may be the case that no moves are possible for the token in question while the other side does have moves.

#In the input, 'X', 'O' are synonymous with 'x', 'o', respectively.  Any version should be acceptable to your script.  That is: ignore case.

#At a minimum, to complete the 100 tests, the submitted script should run all the tests within 60 seconds and achieve at least 80% throughout the testing.

import sys;args = sys.argv[1:]

moveBoards = {}
movesInds = []
if args == []:
    default = '.' * 27 + 'ox......xo' + '.' * 27
    startTok = ''
elif len(args) > 1:
    startTok = args[1].replace('\'', '').replace(']', '')
    default = args[0].replace('\'', '').replace('[', '').replace(',', '')
    default = default.lower()
else:
    default = args[0].replace('\'', '').replace('[', '').replace(',', '').replace(']', '')
    default = default.lower()
    startTok = ''
    if len(default) == 1:
        startTok = default
        default = '.'*27 + 'ox......xo' + '.'*27

startTok = startTok.lower()


lenDef = [i for i in range(0, len(default))]
for i in lenDef:
    if i % 8 == 7: moveBoards[i] = {i - 1, i - 8, i + 8, i + 7, i - 9}.intersection(lenDef)
    elif i % 8 == 0: moveBoards[i] = {i + 1, i - 8, i + 8, i - 7, i + 9}.intersection(lenDef)
    else: moveBoards[i] = {i - 1,i + 1, i - 8, i + 8, i - 7, i + 7, i - 9, i + 9}.intersection(lenDef)

for moveInd in lenDef:
    miniBoard = {n: [] for n in moveBoards[moveInd]}
    for n in moveBoards[moveInd]:
        dis = moveInd - n
        curr = n + dis
        temp = n
        while -1 < curr < 64 and curr in moveBoards[temp]:
            if curr != moveInd:
                miniBoard[n].append(curr)
            temp = curr
            curr = curr + dis
        if len(miniBoard[n]) == 0: del miniBoard[n]
    movesInds.append(miniBoard)

moveBoards = {i: {j for j in movesInds[i]} for i in moveBoards}
getRid = {}
for i in moveBoards:
    if len(moveBoards[i]) == 0:
        getRid[i] = i
for i in getRid:
    del moveBoards[i]

def findTokens(gameB):
    if gameB.count('.') % 2 == 0:return 'x', 'o'
    return 'o', 'x'

def isValid(player, current, possible, gameB):
    movesIndPoss = movesInds[possible][current]
    for i in movesIndPoss:
        if gameB[i] == '.': return False
        elif gameB[i] == player: return True
    return False

def formatMoves(gameB, moveSet):
    askBoard = ''.join([ch if idx not in moveSet else '*' for idx, ch in enumerate(gameB)])
    for i in range(0, 64, 8): print(' '.join(askBoard[i:i+8]))

def formatPoss(passSet):
    return ", ".join([str(i) for i in sorted(passSet)])

def findPossMoves(gameB, player):
    moveSet = set()
    if player != '':
        sec = 'o' if player == 'x' else 'x'
        tok, secTok = player, sec
    else:
        tok, secTok = findTokens(gameB)
    for ind in moveBoards:
        if gameB[ind] == secTok:
            for n in moveBoards[ind]:
                if gameB[n] == '.':
                    if isValid(tok, n, ind, gameB): moveSet.add(n)
    return len(moveSet), moveSet

canMove, possMoves = findPossMoves(default, startTok)
if canMove:
    print('Possible moves: ', possMoves)
else:
    print('No moves possible.')

# Pooja Somayajula, 4, 2024

