def scorer(grid):
    ansHash = {}
    grpNum = 1
    for i in range(9):
        for j in range(9):
            if grid[i][j] == -1:
                temp = getIsland(grid,(i,j))
                for x,y in temp:
                    if (x,y) in ansHash: break
                    ansHash[(x,y)] = grpNum
                grpNum += 1
    scoreHash = {}
    print(ansHash)
    for i,j in ansHash.keys():
        if ansHash[(i,j)] in scoreHash: 
            scoreHash[ansHash[(i,j)]] += 1
        else:
            scoreHash[ansHash[(i,j)]] = 1
    finalAns = 1
    for x in scoreHash:
        print(x)
        finalAns *= scoreHash[x]
    print(scoreHash)
    return finalAns

def getIsland(g,coord):
    r,c = coord
    if g[r][c] != -1: return []
    tempObs = [ (r,c) ]; island = [ (r,c) ]
    while tempObs:
        r1,c1 = tempObs.pop()    
        if g[r1][c1] != -1: continue
        n = getNeigh((r1,c1))
        for n1,n2 in n:
            if g[n1][n2] == -1: 
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

def getCount(grid):
    ans = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0: ans += 1
    return ans
def getSum(grid,direction,r):
    ans = 0
    if direction == 0: #top
        for i in range(9):
            if grid[i][r] != 0: ans += grid[i][r]
            elif ans != 0: return ans
    elif direction == 1: #rhs
        for i in range(8,-1,-1):
            if grid[r][i] != 0: ans += grid[r][i]
            elif ans != 0: return ans        
    elif direction == 2: #bot
        for i in range(8,-1,-1):
            if grid[i][r] != 0: ans += grid[i][r]
            elif ans != 0: return ans        
    elif direction == 3: #lhs
        for i in range(9):
            if grid[r][i] != 0: ans += grid[r][i]
            elif ans != 0: return ans        
    return ans

def printer(y):
    print("   0  1  2  3  4  5  6  7  8 ")
    for cnt in range(9):
        row = y[cnt]
        strr = str(cnt) + "|"
        for i in range(9):
            if row[i] == -1: strr += "x"
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
    top = (41,8,0,0,14,0,15,0,0)
    rhs = (25,0,0,0,10,0,0,0,27)
    bot = (0,9,0,17,0,15,0,35,0)
    lhs = (0,0,25,0,15,0,26,0,0)
    return (top,rhs,bot,lhs)
