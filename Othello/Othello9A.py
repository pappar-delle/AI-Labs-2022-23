import sys;args = sys.argv[1:]
# Pooja Somayajula and Ankita Saxena
# pd 7
# 2/15/23

if len(args) == 2:
    puzzle = args[0]
    width = int(args[1])
    height = len(puzzle)
else:
    puzzle = args[0]
    pzLen = len(puzzle)
    height = max([n for n in range(1, round(pzLen ** 0.5) + 1) if pzLen % n == 0])
    width = int(pzLen/height)

tranformations = set()
tranformations.add(puzzle)

# helper methods
def matToString(matrix):
    s = ''
    for row in range(len(matrix)):
        s += ''.join([str(i) for i in matrix[row]])
    return s

def stringToMat(str_mat, width):
    matrix = []
    for r in range(int(len(str_mat) / width)):
        row = []
        for col in range(width):
            row.append(str_mat[r * width + col])
        matrix.append(row)
    return matrix

universal = stringToMat(puzzle, width)


def rotateCCW(matrix):
    w = len(matrix[0])
    transformed = [[0 for i in range(len(matrix))] for j in range(w)]
    for row in range(len(matrix)):
        for col in range(w):
            transformed[w - col - 1][row] = matrix[row][col]
    return transformed

def rotateCW(matrix):
    return rotateCCW(flipUp(matrix))

def flipUp(matrixix):
    return rotateCCW(rotateCCW(matrixix))

def flipVert(matrix):
    w = len(matrix[0])
    transformed = [[0 for i in range(w)] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(w):
            transformed[row][w - col - 1] = matrix[row][col]
    return transformed

def flipHor(matrix):
    width = len(matrix[0])
    height = len(matrix)
    transformed = [[0 for i in range(width)] for j in range(len(matrix))]
    for row in range(height):
        for col in range(width):
            transformed[height - row - 1][col] = matrix[row][col]
    return transformed

def diagPos(matrix):
    return flipVert(rotateCCW(matrix))

def diagNeg(matrix):
    return flipHor(rotateCCW(matrix))


tranformations.add(matToString(rotateCW(universal)))
tranformations.add(matToString(rotateCCW(universal)))
tranformations.add(matToString(flipUp(universal)))
tranformations.add(matToString(flipVert(universal)))
tranformations.add(matToString(flipHor(universal)))
tranformations.add(matToString(diagNeg(universal)))
tranformations.add(matToString(diagPos(universal)))



for i in tranformations:
    print(i)

# Pooja Somayajula, 4, 2024
