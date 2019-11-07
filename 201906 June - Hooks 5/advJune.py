from basicJune import getSum, printer, getGrid, getParams
from copy import deepcopy as dc, copy as c
from heapq import heappush as hpush, heappop as hpop, heapify
import numpy as np

def getRotatedGrps(grps,direction,coord1,coord2,lvl):
    r1,c1 = coord1; r2,c2 = coord2    
#    4 combinations:
#    _            _
#     |, _|, |_, |
    grps1 = dc(grps)
    if direction == 0:
        grps1[r1][c1:c2+1] = [lvl]*(c2+1-c1)
        for i in range(lvl): grps1[r1+i][c2] = lvl
    elif direction == 1:
        grps1[r2][c1:c2+1] = [lvl]*(c2+1-c1)
        for i in range(lvl): grps1[r1+i][c2] = lvl
    elif direction == 2:
        grps1[r2][c1:c2+1] = [lvl]*(c2+1-c1)
        for i in range(lvl): grps1[r1+i][c1] = lvl
    elif direction == 3:
        grps1[r1][c1:c2+1] = [lvl]*(c2+1-c1)
        for i in range(lvl): grps1[r1+i][c1] = lvl
    return grps1

def grpsChk(grps,params,switchBool,finalAns):
    grps2 = np.transpose(grps)
    if switchBool: 
        finalAns2 = np.transpose(finalAns)
    else:
        finalAns = grps
    collateArr = [] # direction, idx, temp, flipBool, insertBool
    for i in range(9):
        temp3 = c(list(grps[i]))
        temp1 = c(temp3)
        temp1.reverse()
        temp0 = c(list(grps2[i]))
        temp2 = c(temp0)
        temp2.reverse()
        
        temp3a = temp3
        temp2a = temp2
        temp1a = temp1
        temp0a = temp0
        if switchBool:
            temp3a = c(list(finalAns[i]))
            temp1a = c(temp3)
            temp1a.reverse()
            temp0a = c(list(finalAns2[i]))
            temp2a = c(temp0)
            temp2a.reverse()        
        if params[3][i] != 0 and 0 not in temp3: collateArr.append([3,i,temp3,False,True,temp3a])
        if params[1][i] != 0 and 0 not in temp1: collateArr.append([1,i,temp1,True,True,temp1a])
        if params[0][i] != 0 and 0 not in temp0: collateArr.append([0,i,temp0,False,False,temp0a])
        if params[2][i] != 0 and 0 not in temp2: collateArr.append([2,i,temp2,True,False,temp2a])
    while collateArr:
        direction, idx, temp, flipBool, insertBool, tempA = hpop(collateArr)
        if params[direction][idx] != 0:
            boolAns, tempCorrection, n = sumInspector(temp,params[direction][idx],switchBool,tempA)
            if flipBool: tempCorrection.reverse()
            if boolAns: 
                for jj in range(9): 
                    if switchBool and tempCorrection[jj] == 0: continue
                    if insertBool:
                        if finalAns[idx][jj] != -1: finalAns[idx][jj] = tempCorrection[jj]
                    else:
                        if finalAns[jj][idx] != -1: finalAns[jj][idx] = tempCorrection[jj]                    
            else: return [False,None]  
    return [True,finalAns]

def sumInspector(holdingListX,inspectNum,switchBool,finalListX):
    if inspectNum == 0: return [True,holdingListX, 0]
    holdingList = c(holdingListX)
    finalList = c(finalListX)
    moveCounter = 0; iDX = -1; jDX = -1; finalCounter = 0
    for i in range(9):
        finalBool = False
        total = 0
        if holdingList[i] == -1 or finalList[i] == -1: continue
        for j in range(i,9):
            if finalList[i] > 0: finalBool = True
            if holdingList[j] == -1: 
                if moveCounter == 0: holdingList[i] = -1
                if switchBool:
                    if finalBool:
                        if finalCounter == 1:
                            temp = c(holdingList)
                            temp[:iDX] = [-1]*iDX
                            if jDX < 8: temp[jDX+1] = -1
                            if switchBool and jDX < 7: temp[jDX+2:] = [0]*(7-jDX)
                            return [True,temp, 1]                            
                break
            total += holdingList[j]
            if total == inspectNum:
                if switchBool:
                    if moveCounter == 0: iDX = i; jDX = j  
                    if finalBool: finalCounter += 1
                else:
                    iDX = i; jDX = j
                    if moveCounter == 1: return [True,holdingList, 2]
                moveCounter += 1
                break
            elif total > inspectNum:
                if moveCounter == 0: holdingList[i] = -1
                break
    if moveCounter == 1:
        temp = c(holdingList)
        temp[:iDX] = [-1]*iDX
        if jDX < 8: temp[jDX+1] = -1
        if switchBool and jDX < 7: temp[jDX+2:] = [0]*(7-jDX)
        return [True,temp, 1]
    if switchBool and moveCounter > 1: return [True,[0]*9, 2]
    return [False,holdingList, 0]
    
def clearPath(grid, coord):
    c1,c2 = coord
    temp = grid[c1][c2]
    grid[c1][c2] = -1
    numCount = 81
    g1,g2 = -1,-1
    for i in range(9):
        for j in range(9):
            if grid[i][j] == -1: numCount -= 1
            if grid[i][j] >= 0: g1=i; g2=j
    if g1 == -1: return False
    boolAns = numCount == traverseGrid(grid,(g1,g2),{})
    grid[c1][c2] = temp    
    return boolAns

def traverseGrid(grid,coord,visited):
    c1,c2 = coord
    if grid[c1][c2] != -1 and coord not in visited:
        visited[(c1,c2)] = True
        if c1 < 8: traverseGrid(grid,(c1+1,c2),visited)
        if c2 < 8: traverseGrid(grid,(c1,c2+1),visited)
        if c1 > 0: traverseGrid(grid,(c1-1,c2),visited)
        if c2 > 0: traverseGrid(grid,(c1,c2-1),visited)
    return len(visited)
