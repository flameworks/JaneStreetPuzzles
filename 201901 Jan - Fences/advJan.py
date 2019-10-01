import time
from copy import deepcopy as dc, copy
from basicJan import getGrid, printer, counter, getNeigh, getDiagNeigh

def main():
    g = getGrid()
    prevCount = 0
    while prevCount < counter(g):
        prevCount = counter(g)
        borders = []
        for i in range(17):
            for j in range(17):
                if i == 0 or i == 16 or j == 0 or j == 16: borders.append((i,j))
                pole = g[i][j]
                if pole <= 0 or pole == 99: continue
                getBlockedGrid(g,i,j)
        getDeadEnds(g)
        getBottleNeck(g,borders)
        for i in range(17):
            for j in range(17):
                emptySpace = g[i][j]
                if emptySpace != 0: continue
                dcG = dc(g)
                dcG[i][j] = 99
                prevCountDC = 0
                flagBreak = True
                while prevCountDC < counter(dcG):
                    prevCountDC = counter(dcG)
                    borders2 = []
                    for i2 in range(17):
                        if not flagBreak: break
                        for j2 in range(17):
                            if i2 == 0 or i2 == 16 or j2 == 0 or j2 == 16: borders2.append((i2,j2))
                            pole = dcG[i2][j2]
                            if pole <= 0 or pole == 99: continue
                            tempGDC = getBlockedGrid(dcG,i2,j2)
                            if tempGDC == None: 
                                flagBreak = False
                                break
                    if not flagBreak: break
#                    getDeadEnds(dcG)
                    getBottleNeck(dcG,borders2)  
                if not flagBreak: g[i][j] = -99
    print(counter(g))
    return g

def getBottleNeck(g,borders):
    islands = getIslands(g,borders)
    route = getWrap(g,islands)
    islands = getIslands(g,[(7,1)])
    route2 = getWrap(g,islands)       
    finalRoute = list(set(route) & set(route2)) 
    for r1,r2 in finalRoute:
        if g[r1][r2] == 0: g[r1][r2] = 99
    return g

def getIslands(g,islands):
    tempObs = copy(islands)
    while tempObs:
        r1,c1 = tempObs.pop()    
        if g[r1][c1] == 0 or g[r1][c1] == 99: continue
        n = getNeigh((r1,c1))
        for n1,n2 in n:
            if g[n1][n2] != 0 and g[n1][n2] != 99: 
                if (n1,n2) not in islands: 
                    islands.append((n1,n2))
                    tempObs.append((n1,n2))
    return islands

def getWrap(g,islands):
    finalObs = copy(islands)
    while islands:
        r1,c1 = islands.pop()    
        if g[r1][c1] == 0 or g[r1][c1] == 99: continue
        n = getDiagNeigh((r1,c1))
        for n1,n2 in n:
            if g[n1][n2] == 0 or g[n1][n2] == 99: 
                if (n1,n2) not in finalObs: 
                    finalObs.append((n1,n2))
    return list(set(finalObs))
    
def getDeadEnds(g):
    flag = True
    while flag:
        flag = False
        for i in range(17):
            for j in range(17):
                if g[i][j] != 0 and g[i][j] != 99: continue
                temp = getNeigh((i,j))
                ans = 0
                for r,c in temp:
                    if g[r][c] == 0 or g[r][c] == 99: ans += 1
                if ans <= 1: g[i][j] = -99
    return g

def getBlockedGrid(g,i,j):
    pole = g[i][j]       
    topB,rhsB,botB,lhsB = get4d(g,(i,j))
    if i-topB < 0 or i+botB > 16: return None
    if j-lhsB < 0 or j+rhsB > 16: return None    
    for idx in range(i-topB,i+1+botB):
        if idx == i: continue
        if g[idx][j] == -pole: continue
        if g[idx][j] != 0 and g[idx][j] != -99: return None
        g[idx][j] = -pole
    for idx in range(j-lhsB,j+1+rhsB):
        if idx == j: continue
        if g[i][idx] == -pole: continue
        if g[i][idx] != 0 and g[i][idx] != -99: return None
        g[i][idx] = -pole
    return g

def get4d(grid,coord):
    r,c = coord; num = grid[r][c]
    if num <= 0 or num == 99: return (-1,-1,-1,-1)
    LHS,RHS,TOP,BOT = (0,0,0,0)
    for i in range(c):
        if grid[r][i] != 0 and grid[r][i] != -num and grid[r][i] != -99: LHS = i+1
    for i in range(c+1,17):
        if grid[r][i] != 0 and grid[r][i] != -num and grid[r][i] != -99: break
        RHS += 1   
    for i in range(r):
        if grid[i][c] != 0 and grid[i][c] != -num and grid[i][c] != -99: TOP = i+1
    for i in range(r+1,17):
        if grid[i][c] != 0 and grid[i][c] != -num and grid[i][c] != -99: break        
        BOT += 1
    s = (r-TOP,RHS,BOT,c-LHS)
    ans = [0,0,0,0]
    for i in range(4):
        temp = 0
        for j in range(4):
            if j != i: temp += s[j]
        ans[i] = max(num-temp,0)
    return ans

start = time.time()
printer(main())
end = time.time()
print("Time Taken: ",end - start)    

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
