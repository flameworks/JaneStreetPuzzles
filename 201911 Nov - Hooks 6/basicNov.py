import itertools

# GRID METHODS
def countBlocks(grid):
    ans = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == -1: ans += 1
    return ans
            
def getBlockIsland(g,coord):
    r,c = coord
    if g[r][c] > 0: return []
    tempObs = [ (r,c) ]; island = [ (r,c) ]
    while tempObs:
        r1,c1 = tempObs.pop()    
        if g[r1][c1] > 0: continue
        n = getNeigh((r1,c1))
        for n1,n2 in n:
            if g[n1][n2] <= 0: 
                if (n1,n2) not in island: 
                    island.append((n1,n2))
                    tempObs.append((n1,n2))
    return island

def getTempIsland(g):
    for r in range(9):
        for c in range(9):
            if g[r][c] >= 0: break
    tempObs = [ (r,c) ]; island = [ (r,c) ]
    while tempObs:
        r1,c1 = tempObs.pop()    
        if g[r1][c1] == -1: continue
        n = getNeigh((r1,c1))
        for n1,n2 in n:
            if g[n1][n2] >= 0: 
                if (n1,n2) not in island: 
                    island.append((n1,n2))
                    tempObs.append((n1,n2))
    return island

def getIsland(g):
    r = -1
    for i in range(9):
        for j in range(9):
            if g[i][j] > 0:
                r,c = i,j
                break
        if r != -1: break
#    if g[r][c] <= 0: return []
    tempObs = [ (r,c) ]; island = [ (r,c) ]
    while tempObs:
        r1,c1 = tempObs.pop()    
        if g[r1][c1] <= 0: continue
        n = getNeigh((r1,c1))
        for n1,n2 in n:
            if g[n1][n2] > 0: 
                if (n1,n2) not in island: 
                    island.append((n1,n2))
                    tempObs.append((n1,n2))
    return island

def getNeigh(coord):
    r1,c1 = coord
    neigh = []
    if r1 > 0: neigh.append((r1-1,c1))
    if r1 < 8: neigh.append((r1+1,c1))
    if c1 > 0: neigh.append((r1,c1-1))
    if c1 < 8: neigh.append((r1,c1+1))
    return neigh

def getAllCoords():
    ans = []
    for i in range(9):
        for j in range(9):
            ans.append((i,j))
    return ans

def getSplits():
    glob = []
    for i in range(1,9):
        a = list(itertools.combinations(list(range(9)),i))
        for c in a:
            glob.append(c)
    glob.reverse()
    return glob

def printer(y):
    print("   0  1  2  3  4  5  6  7  8 ")
    for cnt in range(9):
        row = y[cnt]
        strr = str(cnt) + "|"
        for i in range(9):
            if row[i] == -1: strr += "."
            if row[i] < 10: strr += " "
            if row[i] == 0: strr += " "
            if row[i] > 0: strr += str(row[i])
            if i < 8: strr += "|"
        strr += "|" + str(cnt)
        print(strr)
    print("   0  1  2  3  4  5  6  7  8 ")

def getGrid():
    return [[0] * 9 for i in range(9)]

def getParams():
    top = (8,0,1,0,2,0,1,0,0)
    rhs = (0,8,0,1,0,9,0,1,0)
    bot = (0,1,0,0,1,0,8,0,0)
    lhs = (9,0,6,5,0,0,0,0,0)
    gcd1 = (top,rhs,bot,lhs)
    
    top1 = (0,0,0,0,0,0,0,42**3,0)
    rhs1 = (0,0,6**2,0,0,0,0,0,0)
    bot1 = (0,0,0,15**2,0,0,0,0,99**2)
    lhs1 = (0,0,0,0,7**3,0,48**2,0,0)
    prod = (top1,rhs1,bot1,lhs1)
    return [gcd1, prod]

