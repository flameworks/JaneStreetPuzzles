from basicNov import printer, getGrid, getSplits, getIsland,getParams,getAllCoords
from advNov import getRotatedGrps, grpsChk, grpsChk3, getConnective, getFillers, getValidSquares
from validNov import paramChk, scorer, sqValidity, numChk, countBlanks
import numpy as np
import time

def main():
    splits = getSplits(); allCoords = getAllCoords()
    workingList = [ [-9, getGrid(),((0,0),(8,8))] ]
    fullMaps = []
    while workingList: # Get full grids
        lvl, numMap, ((r1,c1), (r2,c2)) = workingList.pop(0)
        tempGrps = []
        for i in range(4): tempGrps.append(getRotatedGrps(numMap,i,(r1,c1),(r2,c2),-lvl))
        newCoords = [((r1+1,c1),(r2,c2-1)),((r1,c1),(r2-1,c2-1)),((r1,c1+1),(r2-1,c2)),((r1+1,c1+1),(r2,c2))]
        for i in range(len(tempGrps)):
            if grpsChk(splits,tempGrps[i]): # Check params compatibaility
                if lvl == -1: fullMaps.append(tempGrps[i])
                else: workingList.append([lvl+1, tempGrps[i], newCoords[i]])
    print("Number of stable grids found:",len(fullMaps))
    gcdParam, prodParam = getParams()
    for numMap in fullMaps:
        print("Testing...")
        cleanMap = getGrid()
        while not numChk(cleanMap):
            validNum = grpsChk3(numMap,cleanMap,gcdParam,prodParam,splits) # Check params compatibaility
            if not validNum: break
            getConnective(numMap,cleanMap,allCoords) # Fill all important connective cells
            getFillers(numMap,cleanMap) # Fill all last nums
            getValidSquares(cleanMap) # Ensure Valid Squares
        if validNum: break
    
    # Final Checks
    numBool = numChk(cleanMap)
    scoreBool = countBlanks(cleanMap) == np.sum(scorer(cleanMap))
    paramBool = paramChk(splits,cleanMap,True)
    islandBool = 81-countBlanks(cleanMap) == len(getIsland(cleanMap))
    sqBool = sqValidity(cleanMap)
    finalCheck = scoreBool and numBool and paramBool and islandBool and sqBool
    printer(cleanMap)
    print("Score Check:",scoreBool)    
    print("Numbers Check:",numBool)
    print("Param Check:",paramBool)
    print("Valid Island:",islandBool)
    print("Spacing Check:",sqBool)
    print("@@ OVERALL CHECK:",finalCheck, "@@")
    if not finalCheck: print("@@@@@@@@ERROR@@@@@@@@")
    print("Areas of empty cells:",scorer(cleanMap))
    return cleanMap
    
start = time.time()
x = main()
end = time.time()
print("Time Taken: ",end - start)    
