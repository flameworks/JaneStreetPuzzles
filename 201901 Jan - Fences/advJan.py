import time
import numpy as np
from copy import deepcopy as dc, copy
from heapq import heappush as hpush, heappop as hpop, heapify
from basicJan import getGrid, getGrps, printer, counter, scorer, verifyGrid, getNeigh, getDiagNeigh

def main():
    g = getGrid()
    flag = True
    borders = []
    while flag:
        flag = False
        for i in range(17):
            for j in range(17):
                if i == 0 or i == 16 or j == 0 or j == 16: borders.append((i,j))
                pole = g[i][j]
                if pole <= 0 or pole == 99: continue
                flag, g = getBlockedGrid(g,i,j,flag)
        getDeadEnds(g)
        getBottleNeck(g,borders)
    print(counter(g))
    return g

def getBottleNeck(g,borders):
    islands = getIslands(g,borders)
    route = getWrap(g,islands)
    islands = getIslands(g,[(7,1)])
    route2 = getWrap(g,islands)       
    finalRoute = list(set(route) & set(route2)) 
    for r1,r2 in finalRoute:
        g[r1][r2] = 99
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

def getBlockedGrid(g,i,j,flag):
    pole = g[i][j]
    topB,rhsB,botB,lhsB = get4d(g,(i,j))
    if i-topB < 0: print("ERROR@@@@@@")
    for idx in range(i-topB,i):
        if g[idx][j] == -pole: continue
        if g[idx][j] != 0 and g[idx][j] != -99: print("GG@@@@@")
        g[idx][j] = -pole
        flag = True
    if i+botB > 16: print("ERROR@@@@@@")
    for idx in range(i+1,i+1+botB):
        if g[idx][j] == -pole: continue
        if g[idx][j] != 0 and g[idx][j] != -99: print("GG@@@@@@")
        g[idx][j] = -pole
        flag = True
    if j-lhsB < 0: print("ERROR@@@@@")
    for idx in range(j-lhsB,j):
        if g[i][idx] == -pole: continue
        if g[i][idx] != 0 and g[i][idx] != -99: print("GG@@@@@@")
        g[i][idx] = -pole
        flag = True              
    if j+rhsB > 16: print("ERROR@@@@@@")
    for idx in range(j+1,j+1+rhsB):
        if g[i][idx] == -pole: continue
        if g[i][idx] != 0 and g[i][idx] != -99: print("GG@@@@@@")
        g[i][idx] = -pole
        flag = True        
    return [flag,g]

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
