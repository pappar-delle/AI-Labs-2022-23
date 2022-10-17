import sys; args = sys.argv[1:]
import time

startTime = time.time()

def swapNum(list, c1, c2):
    list[c1[0]][c1[1]], list[c2[0]][c2[1]] = list[c2[0]][c2[1]], list[c1[0]][c1[1]]
    return list

def neighbors(puzzle):
    gWIDTH = findDem(puzzle)[0]
    i_under = [int(puzzle.index("_") / gWIDTH), puzzle.index("_") % gWIDTH]
    puzz_grid = []
    for i in range(gWIDTH):
        puzz_grid.append(list(puzzle)[gWIDTH * i: gWIDTH * (i + 1)])
    return [swapNum([i[:] for i in puzz_grid],i_under, j) for j in [[i_under[0],i_under[1]+1],[i_under[0],i_under[1]-1],[i_under[0]+1,i_under[1]],[i_under[0]-1,i_under[1]]] if j[0]>=0 and j[0]<gWIDTH and j[1]>=0 and j[1]<gWIDTH]

def solve(puzzle, goal):
    if goal == "":
        goal = findDefGoal(puzzle)
    if puzzle == goal:
        listhelp = makeGrid(puzzle)
        print("\n".join(i for i in listhelp))
        print("\n")
        return "Steps: " + str(0)
    if isSolvable(puzzle, goal) == False:
        listhelp = makeGrid(puzzle)
        print("\n".join(i for i in listhelp))
        print("\n")
        return "Steps: " + str(-1)
    parseMe = [puzzle]
    dictSeen = {puzzle:""}
    while parseMe:
        itm = parseMe.pop(0)
        for unseen in neighbors(toString(itm)):
            if toString(unseen) == goal:
                dictSeen[toString(unseen)] = toString(itm)
                counter = makePath(dictSeen, toString(unseen))
                return "Steps: " + str(counter - 1)

            if toString(unseen) not in dictSeen:
                dictSeen[toString(unseen)] = toString(itm)
                parseMe.append(unseen)

    listhelp = makeGrid(puzzle)
    print("\n".join(i for i in listhelp))
    print("\n")
    return "Steps: " + str(-1)

def makePath(dctSeen, goal):
    lister = []
    current_val = goal
    lister.append(current_val)
    while current_val != '':
        current_val = dctSeen[current_val]
        if current_val != '':
            lister.append(current_val)
    lister.reverse()
    j = makeGrid(lister[0])
    len_i = len(j)
    for k in range(0, len(lister), 7):
        for j in range(len_i):
            end = k + 7
            if end >= len(lister):  # makes sure endPt is valid
                end = len(lister)  # make sure its a valid index, if not, set it to length of lister
            partOfLister = [lister[i] for i in range(k, end)]#list of puzzles from lister with indexes in range of(k,endIndex)
            lst = []
            for c in partOfLister:
                grid = makeGrid(c)
                lst.append(grid[j])
            print(" ".join(lst))
            #print everything in lst with spaces in between the items in lst
        print("\n")#print a blank line (good for formatting


    return len(lister)

def findDem(puz):
    x = len(puz)
    lister = [i for i in range(1, x + 1) if x % i == 0]
    width = 0
    height = 0
    if len(lister) % 2 == 0:
        width = lister[int((len(lister) - 1) / 2)]
        height = lister[int((len(lister) - 1) / 2) + 1]
    else:
        width = height = lister[int((len(lister) - 1) / 2)]

    return [width, height]

def makeGrid(strin):
    call = findDem(strin)
    width = call[0]
    height = call[1]
    listhelp = []
    for x in range(width):
        listhelp.append(strin[0:height])
        strin = strin[height:]
    return listhelp

def toString(puzzle):
    return ''.join([''.join(i) for i in puzzle])

def findDefGoal(puzzle):
    lister = [x for x in puzzle]
    lister.sort()
    return ''.join(lister)

def isSolvable(pzl, goal):
    puzz = [i for i in pzl]
    get_to = [i for i in goal]
    ind_puzz = puzz.index('_')
    ind_goal = get_to.index('_')
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
        p_list = makeGrid(pzl)
        g_list = makeGrid(goal)
        num1 = [i for i in range(len(p_list)) if '_' in p_list[i]]
        num2 = [i for i in range(len(p_list)) if '_' in g_list[i]]
        return True if ((p_inv_count + num1[0]) % 2) == ((g_inv_count + num2[0]) % 2) else False

#print(solve('14725368_', '12345678_'))
if len(args) == 1:
    print(solve(args[0], ""))
else:
    print(solve(args[0], args[1]))

time = time.time() - startTime
print("Time: " + "{0:.3g}".format(time) + "s")

# Pooja Somayajula, 4, 2024
