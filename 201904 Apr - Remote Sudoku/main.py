import time
import numpy as np
def main():
    g = getGrid();      tempG = getGrid();    
    pos = getPosGrid(); grps = getGrps()
    filled = [[False] * 10 for i in range(9)]
    while not gridFill(g):
        flag = False
        for i in range(9):
            for j in range(9):
                num = pos[i][j]
                if num != 0:
                    avail = []
                    if i >= num: avail.append((i-num,j))
                    if i+num <= 8: avail.append((i+num,j))
                    if j >= num: avail.append((i,j-num))
                    if j+num <= 8: avail.append((i,j+num))
                    iR,iC,iNum = -1,-1,-1; cnt = 0
                    for r,c in avail:
                        grpNum = grps[r][c]
                        if not filled[grpNum][num]:
                            if g[r][c] == 0:
                                if num not in g[r]:
                                    if num not in tempG[c]:
                                        iR = r; iC = c; iNum = grpNum
                                        cnt += 1
                    if cnt == 1:
                        g[iR][iC] = num
                        pos[i][j] = 0
                        tempG = np.transpose(g)
                        filled[iNum][num] = True
                        flag = True
        if flag: continue
        for i in range(9):
            for j in range(9):
                if g[i][j] == 0:
                    cnt = 0
                    fillNum = 0
                    grpNum = grps[i][j]
                    for num in range(1,10):
                        if filled[grpNum][num]: continue
                        if num in g[i]: continue
                        if num in np.transpose(g)[j]: continue
                        cnt += 1
                        fillNum = num
                    if cnt == 1:
                        g[i][j] = fillNum
                        tempG = np.transpose(g)
                        filled[grpNum][fillNum] = True      
    print("Grid Logic:",verifyGrid(g))
    print("Score:", scorer(g))
    return g
        
def verifyGrid(grid):
    grps = getPosGrid()
    for i in range(9):
        for j in range(9):
            num = grps[i][j]
            cnt = 0
            if num != 0:
                if i >= num and grid[i-num][j] == num: cnt += 1
                if i+num <= 8   and grid[i+num][j] == num: cnt += 1
                if j >= num and grid[i][j-num] == num: cnt += 1
                if j+num <= 8   and grid[i][j+num] == num: cnt += 1
                if cnt == 0: return False
    temp = np.transpose(grid)
    for i in range(9):
        for num in range(1,10):
            if num not in grid[i] or num not in temp[i]: return False
    return True

def scorer(grid):
    ans = 0
    pos = getPosGrid()
    for i in range(9):
        for j in range(9):
            if pos[i][j] != 0:
                ans += grid[i][j] ** 2
    return ans

def gridFill(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0: return False
    return True

def printer(y):
    print("   0  1  2  3  4  5  6  7  8 ")
    for cnt in range(9):
        row = y[cnt]
        strr = str(cnt) + "|"
        for i in range(9):
            if row[i] <= 0: strr += " "
            if row[i] < 10: strr += " "
            if row[i] > 0: strr += str(row[i])
            if i < 8: strr += "|"
        strr += "|" + str(cnt)
        print(strr)
    print("   0  1  2  3  4  5  6  7  8 ")

def getGrps():
    y = getGrid()
    for i in range(9):
        for j in range(9):
            if i > 2: y[i][j] = y[i-3][j] + 3
            elif j > 2: y[i][j] = y[i][j-3] + 1
    return y

def getGrid():
    y = [None] * 9
    for i in range(9):
        y[i] = [0] * 9
    return y

def getPosGrid():
    y = getGrid()
    y[0][0] = 2;    y[0][4] = 7;    y[0][5] = 1;    y[0][6] = 8
    y[0][7] = 3;    y[0][8] = 6;    y[1][7] = 2;    y[2][2] = 5
    y[2][5] = 5;    y[2][6] = 4;    y[2][8] = 2;    y[3][3] = 1
    y[3][6] = 5;    y[3][8] = 1;    y[4][0] = 8;    y[4][1] = 3
    y[4][2] = 3;    y[4][4] = 1;    y[4][6] = 2;    y[4][7] = 4
    y[4][8] = 4;    y[5][0] = 3;    y[5][2] = 4;    y[5][5] = 3
    y[6][0] = 6;    y[6][2] = 2;    y[6][3] = 3;    y[6][6] = 5
    y[7][1] = 4;    y[8][0] = 7;    y[8][1] = 2;    y[8][2] = 7
    y[8][3] = 3;    y[8][4] = 1;    y[8][8] = 3
    return y

start = time.time()
printer(main())
end = time.time()
print("Time Taken: ",end - start)    
