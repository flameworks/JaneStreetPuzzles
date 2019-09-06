import numpy as np
def getSuperNeigh(potArr,coord,x):
    r,c = coord
    grps = getParams()
    tempAns = []
    if r-x >= 0: tempAns.append((r-x,c))
    if r+x <= 8: tempAns.append((r+x,c))
    if c-x >= 0: tempAns.append((r,c-x))
    if c+x <= 8: tempAns.append((r,c+x))
    temp = []
    for tR,tC in tempAns:
        if x in potArr[(tR,tC)]: temp.append((tR,tC))
    grp = grps[getGrpNum(coord,grps)]
    ans = []
    for neigh in temp:
        if neigh not in grp: ans.append(neigh)
    return ans

def scorer(grid):
    arr = [0]*20
    grps = getParams()
    for i in range(9):
        temp = grid[i][0]
        tempGNum = getGrpNum((i,0),grps)
        for j in range(1,9):
            grpNum = getGrpNum((i,j),grps)
            if tempGNum == grpNum:
                temp = temp*10 + grid[i][j]
            else:
                if arr[tempGNum] < temp: arr[tempGNum] = temp
                tempGNum = grpNum
                temp = grid[i][j]
        if arr[tempGNum] < temp: arr[tempGNum] = temp
    print(arr)
    return np.sum(arr)
            
def getGrpNum(coord,grps):
    idx = 0
    for grp in grps:
        if coord in grp: return idx
        idx += 1
    return False
        
def verifyGrid(grid):
    grps = getParams()
    # Check spacing constraint
    for i in range(9):
        for j in range(9):
            num = grid[i][j]
            if i+num <= 8 and grid[i+num][j] == num: continue
            if i-num >= 0 and grid[i-num][j] == num: continue
            if j+num <= 8 and grid[i][j+num] == num: continue
            if j-num >= 0 and grid[i][j-num] == num: continue
            return False
    # Check all spaces filled
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0: return False
    # Check cage constraint
    for grp in grps:
        cnt = list(range(1,len(grp)+1))
        for r,c in grp:
            if grid[r][c] not in cnt: return False
            cnt.remove(grid[r][c])
        if len(cnt) > 0: return False
    # Check initial num constraint
        if grid[1][7] == 1 and grid[2][1] == 3 and grid[3][8] == 2 \
        and grid[4][4] == 1 and grid[5][0] == 2 and grid[6][7] == 4 \
        and grid[7][1] == 2: 
            return True
    return False
    
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

def getGrid():
    y = [None] * 9
    for i in range(9):
        y[i] = [0] * 9
    y[1][7] = 1
    y[2][1] = 3
    y[3][8] = 2
    y[4][4] = 1
    y[5][0] = 2
    y[6][7] = 4
    y[7][1] = 2
    return y

def getParams():
    grp1 = [(0,0),(1,0),(2,0),(3,0),(3,1),(4,1)]
    grp2 = [(0,1),(0,2),(0,3),(1,2),(2,1),(2,2),(2,3),(3,2)]
    grp3 = [(0,4),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4)]
    grp4 = [(0,5)]
    grp5 = [(0,6),(1,6),(2,6)]
    grp6 = [(0,7)]
    grp7 = [(0,8),(1,7),(1,8),(2,7),(2,8),(3,7),(3,8)]
    grp8 = [(1,1)]
    grp9 = [(4,0),(5,0),(5,1),(6,0)]
    grp10 = [(4,2),(5,2),(5,3)]
    grp11 = [(3,3),(4,3)]
    grp12 = [(4,4),(5,4),(6,4)]
    grp13 = [(3,5),(3,6),(4,5),(5,5)]
    grp14 = [(4,6),(5,6)]
    grp15 = [(4,7),(4,8),(5,7),(5,8),(6,7),(6,8)]
    grp16 = [(6,1),(7,0),(7,1),(7,2),(8,0)]
    grp17 = [(6,2),(6,3),(7,3),(7,4),(7,5),(8,1),(8,2),(8,3)]
    grp18 = [(7,6),(8,4),(8,5),(8,6),(8,7)]
    grp19 = [(6,5),(6,6)]
    grp20 = [(7,7),(7,8),(8,8)]
    return (grp1,grp2,grp3,grp4,grp5,grp6,grp7,grp8,grp9,
            grp10,grp11,grp12,grp13,grp14,grp15,grp16,grp17,grp18,grp19,grp20) 
    
