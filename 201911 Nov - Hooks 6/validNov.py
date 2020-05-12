from basicNov import getParams, getBlockIsland
from advNov import getNumArr

def paramChk(splits,numMap,boolChk):
    gcdParam, prodParam = getParams()
    boolAns = True
    for i in range(9):
        a1=True;    a2=True;    a3=True;    a4=True;    
        a5=True;    a6=True;    a7=True;    a8=True
        if prodParam[3][i] != 0: a1 = getNumArr([],numMap[i],True ,True) == prodParam[3][i]
        if prodParam[1][i] != 0: a2 = getNumArr([],numMap[i],False,True) == prodParam[1][i]
        if gcdParam[3][i] != 0: a3 = getNumArr([],numMap[i],True ,False) == gcdParam[3][i] 
        if gcdParam[1][i] != 0: a4 = getNumArr([],numMap[i],False,False) == gcdParam[1][i] 
        tempMap = [row[i] for row in numMap]
        if prodParam[0][i] != 0: a5 = getNumArr([],tempMap,True ,True ) == prodParam[0][i]
        if prodParam[2][i] != 0: a6 = getNumArr([],tempMap,False,True ) == prodParam[2][i]
        if gcdParam[0][i] != 0: a7 = getNumArr([],tempMap,True ,False) == gcdParam[0][i] 
        if gcdParam[2][i] != 0: a8 = getNumArr([],tempMap,False,False) == gcdParam[2][i]
        boolAns = boolAns and (a1 and a2 and a3 and a4 and a5 and a6 and a7 and a8)
        for j in range(9):
            numMap[j][i] = tempMap[j]
    return boolAns

def scorer(grid):
    ansHash = {}
    grpNum = 1
    for i in range(9):
        for j in range(9):
            if grid[i][j] <= 0:
                temp = getBlockIsland(grid,(i,j))
                for x,y in temp:
                    if (x,y) in ansHash: break
                    ansHash[(x,y)] = grpNum
                grpNum += 1
    scoreHash = {}
    for i,j in ansHash.keys():
        if ansHash[(i,j)] in scoreHash: 
            scoreHash[ansHash[(i,j)]] += 1
        else:
            scoreHash[ansHash[(i,j)]] = 1
    finalAns = 1
    ans = []
    for x in scoreHash:
        finalAns *= scoreHash[x]
        ans.append(scoreHash[x])
    print("** SCORE:",'{:,}'.format(finalAns),"**")
    return ans

def numChk(g):
    a = {}
    for i in range(-1,10):
        a[i] = -i
    for i in range(9):
        for j in range(9):
            a[g[i][j]] = a[g[i][j]] + 1
    flag = True
    for x in a:
        if x > 0 and a[x] != 0: 
#            print(x,":",a[x])
            flag = False
            break
    return flag

def sqValidity(g):
    for i in range(1,9):
        for j in range(1,9):
            temp = [g[i-1][j-1],g[i-1][j],g[i][j-1],g[i][j]]
            flag = False
            for num in temp:
                if num <= 0:
                    flag = True
                    break
            if flag: continue
            return False
    return True

def countBlanks(grid):
    ans = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] <= 0: ans += 1
    return ans
