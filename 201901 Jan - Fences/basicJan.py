def getDiagNeigh(coord):
    r1,c1 = coord
    neigh = []
    if r1 > 0: neigh.append((r1-1,c1))
    if r1 < 16: neigh.append((r1+1,c1))
    if c1 > 0: neigh.append((r1,c1-1))
    if c1 < 16: neigh.append((r1,c1+1))
    if r1 > 0 and c1 > 0: neigh.append((r1-1,c1-1))
    if r1 > 0 and c1 < 16: neigh.append((r1-1,c1+1))
    if r1 < 16 and c1 > 0: neigh.append((r1+1,c1-1))
    if r1 < 16 and c1 < 16: neigh.append((r1+1,c1+1))
    return neigh

def getNeigh(coord):
    r1,c1 = coord
    neigh = []
    if r1 > 0: neigh.append((r1-1,c1))
    if r1 < 16: neigh.append((r1+1,c1))
    if c1 > 0: neigh.append((r1,c1-1))
    if c1 < 16: neigh.append((r1,c1+1))
    return neigh

def verifyGrid(grid):
    return True

def scorer(grid):
    ans = 0
    return ans

def counter(grid):
    ans = 0
    for i in range(17):
        for j in range(17):
            if grid[i][j] != 0: ans += 1
    return ans

def printer(y):
    topLine = "   "
    for i in range(17):
        topLine += "  " + str(i)
        if i < 9: topLine += " "
    print(topLine)
    for cnt in range(17):
        row = y[cnt]
        strr = str(cnt) + "|"
        if cnt < 10: strr = " " + str(cnt) + "|"
        for i in range(17):
            if row[i] == 99:
                strr += " @ "
            elif row[i] == -99:
                strr += " .."
            elif row[i] < -9: 
                strr += "x" + str(abs(row[i]))
            elif row[i] < 0:
                strr += " x" + str(abs(row[i]))
            elif row[i] == 0:
                strr += "   "
            elif row[i] < 10:
                strr += "  " + str(row[i])
            else:
                strr += " " + str(row[i])
            strr += "|"
        strr += str(cnt)
        print(strr)
    print(topLine)

def getGrps():
    y = getGrid()
    for i in range(9):
        for j in range(9):
            if i > 2: y[i][j] = y[i-3][j] + 3
            elif j > 2: y[i][j] = y[i][j-3] + 1
    return y

def getGrid():
    y = [None] * 17
    for i in range(17):
        y[i] = [0] * 17
    y[0][5]=2;    y[0][9]=1;    y[0][16]=5;   y[1][7]=3;    y[1][14]=2;    y[2][4]=3
    y[3][0]=5;    y[3][11]=22;  y[4][4]=4;    y[5][9]=4;    y[5][13]=1;    y[6][15]=19
    y[7][7]=15;   y[8][8]=4;    y[9][9]=2;    y[10][1]=9;   y[11][3]=3;    y[11][7]=2
    y[12][12]=4;  y[13][5]=8;   y[13][16]=9;  y[14][12]=4;  y[15][2]=3;    y[15][9]=15
    y[16][0]=6;   y[16][7]=1;   y[16][11]=4
    return y

'''
A 17-by-17 field is divided into unit squares. Some of the squares contain “posts” 
at their center. Each post is represented below by a number. Construct one or more
 fences emanating from each post, such that the total length of fence connected to 
 a post equals the number given. Fences have integer length and can only be constructed
 horizontally or vertically. Fences from different posts may not touch, nor may 
 a fence from one post touch a different post.

The goal of this puzzle is to build your fences in such a manner that it is possible
 to draw a closed loop through some of the remaining empty squares. The loop must 
 enclose at least one post, and must be symmetric in some way (either via
 rotation or reflection). As in the example, the loop must be rectilinear, 
 passing through the centers of adjacent empty squares.

The answer to this puzzle is the product of the fence-lengths of the fences inside
 the loop. (Note that in the Example, the answer is 2, not 4.
'''
