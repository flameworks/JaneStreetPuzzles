def getKnightMoves(coord, idx):
    r,c = coord
    ans = []
    if r-2 >= 0     and c-1 >= 0:       ans.append((r-2,c-1))
    if r-2 >= 0     and c+1 <= idx-1:   ans.append((r-2,c+1))
    if r+2 <= idx-1 and c-1 >= 0:       ans.append((r+2,c-1))
    if r+2 <= idx-1 and c+1 <= idx-1:   ans.append((r+2,c+1))
    if r-1 >= 0     and c-2 >= 0:       ans.append((r-1,c-2))
    if r+1 <= idx-1 and c-2 >= 0:       ans.append((r+1,c-2))
    if r-1 >= 0     and c+2 <= idx-1:   ans.append((r-1,c+2))
    if r+1 <= idx-1 and c+2 <= idx-1:   ans.append((r+1,c+2))
    return ans

def getArr(testCase):
    if testCase == 1:
        idx = 5
        arr = [[0 for x in range(idx)] for y in range(idx)]
        arr[0][0] = 1
        arr[1][4] = 4
        arr[4][1] = 6
        a1 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 2), (2, 3), (2, 4), (3, 4), (4, 3), (4, 4)]
        a2 = [(2,1),(3,0),(3,1),(3,2),(3,3),(4,0)]
        a3 = [(4,1),(4,2)]
        area = (a1,a2,a3)
        maxNum = 6
    else:
        idx = 10
        arr = [[0 for x in range(idx)] for y in range(idx)]
        arr[0][0] = 12;        arr[1][6] = 5;        arr[1][8] = 23
        arr[2][6] = 8;        arr[3][3] = 14;           arr[5][1] = 2
        arr[6][4] = 20;        arr[7][4] = 33;        arr[9][9] = 28
        a1 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (1, 7), (1, 9), (2, 0), (2, 1), (2, 2), (2, 4), (2, 5), (2, 6), (2, 7), (2, 9), (3, 0), (3, 1), (4, 1), (4, 3), (4, 4), (5, 1), (5, 2), (5, 3)];        a2 = [(1, 3), (2, 3), (3, 2), (3, 3), (3, 4), (3, 5), (4, 2)];        a3 = [(1, 8), (2, 8), (3, 7), (3, 8), (3, 9)]
        a4 = [(3, 6), (4, 6), (4, 7), (4, 8), (4, 9), (5, 9)];        a5 = [(4, 5), (5, 4), (5, 5), (5, 6), (6, 4)];        a6 = [(4, 0), (5, 0), (6, 0), (7, 0), (8, 0)];        a7 = [(7, 1), (8, 1), (9, 0), (9, 1)]
        a8 = [(6, 1), (6, 2), (7, 2)];        a9 = [(8, 2), (9, 2)];        a10 = [(6, 3), (7, 3), (7, 4), (8, 3)];        a11 = [(9, 3), (9, 4), (9, 5), (9, 6), (9, 7)];        a12 = [(8, 7), (8, 8), (9, 8)];        a13 = [(8, 4), (8, 5), (8, 6)]
        a14 = [(7, 5), (7, 6), (7, 7)];        a15 = [(6, 5), (6, 6)];        a16 = [(5, 7), (5, 8), (6, 7), (6, 8), (7, 8)];        a17 = [(6, 9), (7, 9), (8, 9), (9, 9)]
        area = (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17)
        maxNum = 33
        
    areaGrid = [[0 for x in range(idx)] for y in range(idx)]
    numIdx = 1
    for A in area:
        for x,y in A:
            areaGrid[x][y] = numIdx
        numIdx += 1
    key = []
    loc = {}
    areaLoc = {}
    sectSums = [0] * len(area)
    areaNum = 0
    for allArea in area:
        for coord in allArea:
            areaLoc[coord] = areaNum
        areaNum += 1    
    for r in range(idx):
        for c in range(idx):
            num = arr[r][c]
            if num != 0:
                key.append( (r,c) )
                loc[ num ] = (r,c)
                sectSums[areaLoc[(r,c)]] += num

    return idx, arr, key, area, areaGrid, maxNum, \
               len(area), loc, areaLoc, sectSums
