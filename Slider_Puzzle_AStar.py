import sys; args = sys.argv[1:]
import time

startTime = time.time()

with open("Eckel.txt") as f:
    listpuzz = [line.strip() for line in f]

gWIDTH, gHEIGHT = 4, 4
goalState = listpuzz[0]
lookUpGoal = {}
for i in range(len(goalState)):
    lookUpGoal[goalState[i]] = i


def swapNum(list, c1, c2):
    newList = list[:]
    newList[c1], newList[c2] = newList[c2], newList[c1]
    return newList

def solve(puzzle, goal):
    if puzzle == goal:
        return {}
    if isSolvable(puzzle, goal) == False:
        return ['S']
    openSet = [set() for i in range(52)]
    i_under = puzzle.index('_')
    openSet[0].add((puzzle, "", 0, i_under, manhattan(puzzle, goal)))
    closedSet = {}
    while True:
        tup = next(nonempty for nonempty in openSet if nonempty).pop()
        itm = tup[0]
        if itm in closedSet:
            continue
        closedSet[itm] = tup[1] #store the item and the parent
        if itm == goal:
            return closedSet

        puzz_grid = list(itm)
        n = []
        if (tup[3] % 4) < (4 - 1):
            n.append((swapNum(puzz_grid, tup[3], tup[3] + 1), tup[3] + 1))
        if (tup[3] % 4) > 0:
            n.append((swapNum(puzz_grid, tup[3], tup[3] - 1), tup[3] - 1))
        if (tup[3] - 4 >= 0):
            n.append((swapNum(puzz_grid, tup[3], tup[3] - 4), tup[3] - 4))
        if (tup[3] + 4 < len(puzzle)):
            n.append((swapNum(puzz_grid, tup[3], tup[3] + 4), tup[3] + 4))


        for unseen in n:
            runseen = toString(unseen[0])
            lvl = tup[2] + 1 #level is manhattan distance from puzzle to start
            if runseen not in closedSet:
                h = tup[4] - small_H(itm, unseen[1]) + small_H(runseen, tup[3])
                openSet[lvl + h].add((runseen, itm, lvl,unseen[1], h))
            #openSet.append((lvl + manhattan(unseen, goal), unseen, itm, lvl)) #store estimate, puzzle, parent, level


#URDLULDDLDRULURDLDRULURDLD
#URDLULDDLDRULURDLDRULURDLD

def makePath(dctSeen, goal):
    lister = []
    current_val = goal
    lister.append(current_val)
    if dctSeen == {}:
        return [goal]
    if dctSeen == ['S']:
        return {}
    while current_val != '':
        current_val = dctSeen[current_val]
        if current_val != '':
            lister.append(current_val)
    lister.reverse()
    return lister

def toString(puzzle):
    return ''.join([''.join(i) for i in puzzle])
def isSolvable(pzl, goal):
    puzz = [i for i in pzl]
    get_to = [i for i in goal]
    puzz.remove('_')
    get_to.remove('_')
    #inv count puzz
    p_inv_count = sum([1 for i in range(len(puzz)) for j in range(i + 1, len(puzz)) if (puzz[i] > puzz[j])])
    #for i in range(len(puzz)):
     #   for j in range(i + 1, len(puzz)):
      #      if puzz[i] > puzz[j]:
       #         p_inv_count += 1
    #inv count goal
    g_inv_count = sum([1 for i in range(len(get_to)) for j in range(i + 1, len(get_to)) if (get_to[i] > get_to[j])])
    #for i in range(len(get_to)):
     #   for j in range(i + 1, len(get_to)):
      #      if (get_to[i] > get_to[j]):
       #         g_inv_count += 1

    if len(pzl) % 2 != 0:
        return True if (p_inv_count % 2) == (g_inv_count % 2) else False
    elif len(pzl) % 2 == 0:
        p_list = [pzl[x:x + gWIDTH] for x in range(0, len(pzl), gWIDTH)]
        g_list = [listpuzz[0][x:x + gWIDTH] for x in range(0, len(listpuzz[0]), gWIDTH)]
        num1 = [i for i in range(len(p_list)) if '_' in p_list[i]]
        num2 = [i for i in range(len(p_list)) if '_' in g_list[i]]
        return True if ((p_inv_count + num1[0]) % 2) == ((g_inv_count + num2[0]) % 2) else False

def condensePath(lstPzl):
    if lstPzl == [goalState]:
        return "G"
    if lstPzl == {}:
        return "X"
    elif len(lstPzl) == 1:
        return "G"
    path = ""
    for i in range(len(lstPzl) - 1):
        p = lstPzl[i]
        g = lstPzl[i + 1]
        indp = p.index('_')
        indg = g.index('_')
        if indp//4 < indg // 4:
            path += 'D'
        elif indp // 4 > indg // 4:
            path += 'U'
        elif indp < indg:
            path += 'R'
        elif indp > indg:
            path += 'L'
    return path


def manhattan(puzz, goal): #abs(x_val - x_goal) + abs(y_val - y_goal)
    h = 0
    for i in puzz:
        if i != '_':
            pui = puzz.index(i)
            gui = goal.index(i)
            h += abs((pui // 4) - (gui // 4)) + abs((pui % 4) - (gui % 4))
    return h

def small_H(puzz, pui):
    gui = lookUpGoal[puzz[pui]]
    return abs((pui // 4) - (gui // 4)) + abs((pui % 4) - (gui % 4))

if __name__ == '__main__':
    for i in listpuzz:
        print(i, condensePath(makePath(solve(i, goalState), goalState)))
        #print(makePath(solve(i, goalState), goalState))

time = time.time() - startTime
print("Time: " + "{0:.3g}".format(time) + "s")

# Pooja Somayajula, 4, 2024
