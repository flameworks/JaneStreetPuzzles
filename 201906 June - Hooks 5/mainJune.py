from basicJune import getSum, printer, getGrid, getParams, getCount, scorer
from advJune import getRotatedGrps, grpsChk, sumInspector, clearPath
from copy import deepcopy as dc, copy as c
from heapq import heappush as hpush, heappop as hpop, heapify
import time

def main():
    params = getParams()
    workingList = [ [-9, getGrid(),(0,0),(8,8)] ]
    firstAns = []
    counter = 0
    while workingList and len(firstAns)==0:
        counter += 1
        heapify(workingList)
        lvl, grps, coord1, coord2 = hpop(workingList)
        r1,c1 = coord1; r2,c2 = coord2; tempGrps = []
        newCoords = [((r1+1,c1),(r2,c2-1)), ((r1,c1),(r2-1,c2-1)),
                     ((r1,c1+1),(r2-1,c2)), ((r1+1,c1+1),(r2,c2))]
        for i in range(4): tempGrps.append(getRotatedGrps(grps,i,coord1,coord2,-lvl))
        for i in range(len(tempGrps)):
            boolAns, newGrp = grpsChk(tempGrps[i],params,False,[])
            if boolAns: boolAns, newGrp = grpsChk(newGrp,params,False,[])
            if boolAns:
                c1,c2 = newCoords[i]
                if lvl == -1: 
                    if newGrp not in firstAns: firstAns.append(newGrp)
                else: hpush(workingList,[lvl+1, newGrp,c1,c2])
    for overallGrps in firstAns:
        boolAns, finalAns = grpsChk(overallGrps,params,True,getGrid())     
        fillCounter = getCount(finalAns)
        currCount = fillCounter
        stepCounter = 1
        
        finalAns[8][6] = 9
        grpsDict = {}
        for i in range(9):
            for j in range(9):
                num = overallGrps[i][j]
                if num > 0:
                    if num in grpsDict: grpsDict[num].append((i,j))
                    else: grpsDict[num] = [(i,j)]
        while stepCounter > 0:
            fillCounter = currCount                
    ###        if a certain cell creates 4-island, fill -1
            for i in range(1,9):
                for j in range(1,9):
                    fourCoords = [(i-1,j-1),(i,j-1),(i-1,j),(i,j)]
                    flag = False; z1 = -1; z2 = -1; intCounter = 0
                    for c1,c2 in fourCoords: 
                        if finalAns[c1][c2] == -1: flag = True
                        if finalAns[c1][c2] == 0: z1 = c1; z2 = c2
                        if finalAns[c1][c2] > 0: intCounter += 1
                    if flag: continue
                    if intCounter == 3: 
                        finalAns[z1][z2] = -1
                        overallGrps[z1][z2] = -1
    ###        if specified number cant be filled, fill -1 for all unopen numbers
            numCounter = [0]*10        
            for i in range(9):
                for j in range(9):
                    if finalAns[i][j] > 0: numCounter[finalAns[i][j]] += 1                        
            for num in range(1,10):
                if numCounter[num] == num:
                    for i in range(9):
                        for j in range(9):
                            if overallGrps[i][j] == num and finalAns[i][j] != num:
                                finalAns[i][j] = -1
                                overallGrps[i][j] = -1
    ###        if specified number CAN be filled, fill all numbers
            for num in range(1,10):
                zCount = 0
                for c1,c2 in grpsDict[num]:
                    if finalAns[c1][c2] == 0: zCount += 1
                if num - numCounter[num] == zCount:
                    for c1,c2 in grpsDict[num]:
                        if finalAns[c1][c2] == 0: finalAns[c1][c2] = num
    ##       if a X blocks path, place number.
            for i in range(9):
                for j in range(9):
                    if finalAns[i][j] == 0:
                        if not clearPath(finalAns,(i,j)):
                            finalAns[i][j] = overallGrps[i][j]
    ###       fill in based on params and merge with finalAns
            boolAns, tempFinalAns = grpsChk(overallGrps,params,True,finalAns)
            if not boolAns: return "ERROR"
            for i in range(9):
                for j in range(9):
                    if tempFinalAns[i][j] != 0: 
                        if finalAns[i][j] != tempFinalAns[i][j]:
                            finalAns[i][j] = tempFinalAns[i][j]
            currCount = getCount(finalAns)            
            stepCounter = currCount - fillCounter
    print(currCount,numCounter)
    return finalAns
    
start = time.time()
x = main()
end = time.time()
#print(len(x))
printer(x)
print(scorer(x))
print("Time Taken: ",end - start)    
