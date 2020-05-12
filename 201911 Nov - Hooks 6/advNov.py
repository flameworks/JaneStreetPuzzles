from basicNov import getParams
from copy import deepcopy as dc
from basicNov import getTempIsland

def getRotatedGrps(grps,direction,coord1,coord2,lvl):
    r1,c1 = coord1; r2,c2 = coord2    
#    4 combinations:
#    _            _
#     |, _|, |_, |
    grps1 = dc(grps)
    if coord1 == coord2 and direction != 0: return None
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

def gcd(x, y):
    while y != 0: (x, y) = (y, x % y)
    return x

def getNumArr(splitCoord,rowArr,direction,action):
    if not direction: rowArr.reverse()
    gcdNum = 0; prodNum = 1; temp = 0
    for idx in range(9):
        num = rowArr[idx]
        if idx in splitCoord or num <= 0:
            if temp != 0: prodNum *= temp
            if not action: gcdNum = gcd(gcdNum,temp)
            temp = 0
        else:
            temp = temp * 10 + num
    if temp != 0: prodNum *= temp
    if not action: gcdNum = gcd(gcdNum,temp)
    if not direction: rowArr.reverse()
    if action: return prodNum
    return gcdNum

def rowChk(rw,direction,action,paramNum,splits):
    if paramNum == 0: return True
    for coord in splits: 
        if getNumArr(coord,rw,direction,action) == paramNum: return True
    return False

def grpsChk(splits,numMap):
    gcdParam, prodParam = getParams() # gcd1 = (top,rhs,bot,lhs)
    if numMap == None: return False
    for i in range(9):
        if 0 not in numMap[i]:
            if not rowChk(numMap[i],True ,True ,prodParam[3][i],splits): return False # PROD LHS
            if not rowChk(numMap[i],False,True ,prodParam[1][i],splits): return False # PROD RHS
            if not rowChk(numMap[i],True ,False,gcdParam[3][i] ,splits): return False # GCD LHS
            if not rowChk(numMap[i],False,False,gcdParam[1][i] ,splits): return False # GCD RHS
        tempMap = [row[i] for row in numMap]
        if 0 not in tempMap:
            if not rowChk(tempMap,True ,True ,prodParam[0][i],splits): return False # PROD TOP
            if not rowChk(tempMap,False,True ,prodParam[2][i],splits): return False # PROD BOT
            if not rowChk(tempMap,True ,False,gcdParam[0][i] ,splits): return False # GCD TOP
            if not rowChk(tempMap,False,False,gcdParam[2][i] ,splits): return False # GCD BOT
    return True

def rowChk3(origRow,cleanRow,direction,action,paramNum,splits):
    if paramNum == 0: return 1
    gdCoords = []
    if not direction: 
        origRow.reverse()
        cleanRow.reverse()
    for coord in splits:
        flag = False
        for c in range(9):
            if cleanRow[c] == -1 and c not in coord:
                flag = True
                break
        if flag: continue
        for c in coord:
            if cleanRow[c] > 0: 
                flag = True
                break
        if flag: continue
        if getNumArr(coord,origRow,True,action) == paramNum: gdCoords.append(coord)
    if len(gdCoords) != 0:
        allPts = set(range(9))
        allBlock = set(gdCoords[0])
        for coord in gdCoords:
            allPts -= set(coord)
            allBlock &= set(coord)    
        for c in allPts: cleanRow[c] = origRow[c]
        for c in allBlock: cleanRow[c] = -1
        if not direction: 
            origRow.reverse()
            cleanRow.reverse()
    return len(gdCoords)

def grpsChk3(numMap,cleanMap,gcdParam, prodParam,splits):
    validNum = 1
    for i in range(9): # Validity of inputs
        validNum *= rowChk3(numMap[i],cleanMap[i],True,True,prodParam[3][i],splits)
        validNum *= rowChk3(numMap[i],cleanMap[i],False,True,prodParam[1][i],splits)
        validNum *= rowChk3(numMap[i],cleanMap[i],True,False,gcdParam[3][i],splits)
        validNum *= rowChk3(numMap[i],cleanMap[i],False,False,gcdParam[1][i],splits)
        if validNum == 0: break
        tempMap = [row[i] for row in numMap]    
        tempClean = [row[i] for row in cleanMap]    
        validNum *= rowChk3(tempMap,tempClean,True,True,prodParam[0][i],splits)
        validNum *= rowChk3(tempMap,tempClean,False,True,prodParam[2][i],splits)
        validNum *= rowChk3(tempMap,tempClean,True,False,gcdParam[0][i],splits)
        validNum *= rowChk3(tempMap,tempClean,False,False,gcdParam[2][i],splits)
        if validNum == 0: break
        for j in range(9):
            numMap[j][i] = tempMap[j]    
            cleanMap[j][i] = tempClean[j]     
    return validNum != 0

def getConnective(numMap,cleanMap,allCoords): # Fill all important connective cells
    for i in range(9): 
        for j in range(9):
            if cleanMap[i][j] != 0: continue
            cleanMap[i][j] = -1
            unseenCoords = set(allCoords) - set(getTempIsland(cleanMap))
            cleanMap[i][j] = 0
            for a,b in unseenCoords:
                if cleanMap[a][b] > 0:
                    cleanMap[i][j] = numMap[i][j]
                    break
            
def getFillers(numMap,cleanMap): # Fill all last nums
    cntArr = [];    zCoordsArr = []
    for i in range(11):
        cntArr.append(0)
        zCoordsArr.append([])
    for i in range(9):
        for j in range(9):
            num = numMap[i][j]
            if cleanMap[i][j] == 0: zCoordsArr[num].append((i,j))
            elif cleanMap[i][j] == num: cntArr[num] += 1
    for num in range(1,10):
        if len(zCoordsArr[num]) + cntArr[num] == num:
            for i,j in zCoordsArr[num]: cleanMap[i][j] = num
        elif cntArr[num] == num:
            for i,j in zCoordsArr[num]: cleanMap[i][j] = -1
                
def getValidSquares(cleanMap): # Ensure Valid Squares
    for i in range(1,9): 
        for j in range(1,9):
            temp = [(i-1,j-1),(i-1,j),(i,j-1),(i,j)]
            cnt = 0; zCoords = []
            for i,j in temp:
                num = cleanMap[i][j]
                if num == 0: zCoords.append((i,j))
                if num > 0: cnt += 1
            if cnt == 3:
                for i,j in zCoords: cleanMap[i][j] = -1     
                
