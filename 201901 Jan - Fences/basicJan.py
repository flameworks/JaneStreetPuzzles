import time
import numpy as np
from copy import deepcopy as dc
from heapq import heappush as hpush, heappop as hpop, heapify

def main():
    g = getGrid()
    flag = True
    while flag:
        flag = False
        for i in range(17):
            for j in range(17):
                pole = g[i][j]
                if pole <= 0 or pole == 99: continue
                flag, g = getBlockedGrid(g,i,j,flag)
        getDeadEnds(g)
        getBottleNeck(g)
    print(counter(g))
 
    return g

def getBottleNeck(g):
    return g
        
def getNeigh(coord):
    r1,c1 = coord
    neigh = []
    if r1 > 0: neigh.append((r1-1,c1))
    if r1 < 16: neigh.append((r1+1,c1))
    if c1 > 0: neigh.append((r1,c1-1))
    if c1 < 16: neigh.append((r1,c1+1))
    return neigh

def dijk(g,coord1,coord2):
    dist = {}; prev = {}; visited = {}
    for i in range(17):
        for j in range(17):
            dist[(i,j)] = 999
            prev[(i,j)] = None
            visited[(i,j)] = False
    dist[coord1] = 0
    visited[coord1] = True
    prev[coord1] = False
    temp = [ [0,coord1] ]
    while temp:
        d, tempCoord = hpop(temp)
        r1,c1 = tempCoord
        if coord2 == tempCoord: break
        visited[tempCoord] = True
        neigh = getNeigh(tempCoord)
        for n1,n2 in neigh:
            if g[n1][n2] != 0 and g[n1][n2] != 99: continue
            if visited[(n1,n2)]: continue
            if dist[(n1,n2)] > dist[tempCoord] + 1: 
                dist[(n1,n2)] = dist[tempCoord] + 1
                prev[(n1,n2)] = tempCoord
                hpush(temp,[dist[(n1,n2)],(n1,n2)])
    if dist[coord2] == 999: return []
    route = [coord2]
    while prev[route[-1]]:
        route.append(prev[route[-1]])
    route.reverse()
    return route

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
                strr += " " + str(row[i])
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
