def matrix(n):
    val = [0] * n
    for x in range(0, n):
        val[x] = [0] * n # type: ignore
    return val

def getList(matrix, r, c, dir):
    l = list()
    if dir == 0: #up
        for x in range(0, r):
            l.append(matrix[x][c])
        l.reverse()
    elif dir == 1: #down
        for x in range(r + 1, 99):
            l.append(matrix[x][c])
    elif dir == 2: #left
        for x in range(0, c):
            l.append(matrix[r][x])
        l.reverse()
    else: #right
        for x in range(c+1, 99):
            l.append(matrix[r][x])
    return l

def scenicScoreOne(l, v):
    cnt = 1
    for el in l:
        if el >= v:
            return cnt
        else:
            cnt += 1
    return cnt

def areMinor(l, v):
    for el in l:
        if el >= v:
            return False
    return True

def getScenicScore(matrix, r, c):
    #if r == 0 or r == 98 or c == 0 or c == 98:
    #    return 0
    upperList, downList, leftList, rightList = getList(matrix, r, c, 0), getList(matrix, r, c, 1), getList(matrix, r, c, 2), getList(matrix, r, c, 3)
    return scenicScoreOne(upperList, matrix[r][c]) * scenicScoreOne(downList, matrix[r][c]) * scenicScoreOne(leftList, matrix[r][c]) * scenicScoreOne(rightList, matrix[r][c])

def isVisible(matrix, r, c):
    if r == 0 or r == 98 or c == 0 or c == 98:
        return True
    upperList, downList, leftList, rightList = getList(matrix, r, c, 0), getList(matrix, r, c, 1), getList(matrix, r, c, 2), getList(matrix, r, c, 3)
    return areMinor(upperList, matrix[r][c]) or areMinor(downList, matrix[r][c]) or areMinor(leftList, matrix[r][c]) or areMinor(rightList, matrix[r][c])

def main(f):
    mat = matrix(99)
    
    rows = f.split('\n')
    cntR, cntC = 0, 0
    for row in rows:
        for cell in row:
            mat[cntR][cntC] = cell # type: ignore
            cntC += 1
        cntC = 0
        cntR += 1

    tot = 0

    for row in range(0, 99):
        for col in range(0, 99):
            if isVisible(mat, row, col):
                tot += 1 #prima sfida

    tot = 0

    for row in range(1, 98):
        for col in range(1, 98):
            tmp = getScenicScore(mat, row, col)
            if tot < tmp:
                tot = tmp #seconda sfida
    
    return tot


f = open("in.txt", "r")
print(main(f.read()))