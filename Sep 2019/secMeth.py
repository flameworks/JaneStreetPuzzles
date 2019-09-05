from basic import getParams, printer, getGrid, verifyGrid
from meths import jamGrid
from copy import deepcopy as dc
import time

def getAllpot(gridInput,itier):
    grid = dc(gridInput)
    grps = getParams()
    potArr = {}
    errorStr = ""
    x = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for grp in grps:
                    if (i,j) in grp:
                        x = len(grp)+1
                        break
                potArr[(i,j)] = list(range(1,x))
            else:
                potArr[(i,j)] = [grid[i][j]]

    for kkz in range(itier):
        # Remove dups in potentials
        potArr = removeDups(potArr)

        # Fill cells that have only 1 num possibility in cage
        for grp in grps:
            for num in range(1,9):
                counter = 0
                counterCoord = (-1,-1)
                for coord in grp:
                    if num in potArr[coord]:
                        counter += 1
                        counterCoord = coord
                if counter == 1:
                    r,c = counterCoord
                    if len(potArr[(r,c)]) > 1:
                        potArr[(r,c)] = [num]
                        potArr = removeDups(potArr)

        # If Multiple, remove options that dont have available neighbours
        # If Single, jam those with singleton Neighbours
        for i in range(9):
            for j in range(9):
                if len(potArr[(i,j)]) > 1:
                    tempHold = dc(potArr[(i,j)])
                    for pot in potArr[(i,j)]:
                        neighArr = getSuperNeigh(potArr,(i,j),pot)
                        if len(neighArr) == 0: tempHold.remove(pot)
                    potArr[(i,j)] = tempHold
                    if len(tempHold) == 0: errorStr += "ERROR 1"
                    if len(potArr[(i,j)]) == 1: potArr = removeDups(potArr)

                elif len(potArr[(i,j)]) == 0: errorStr += "ERROR 2"
                else:
                    num = potArr[(i,j)][0]
                    neighArr = getSuperNeigh(potArr,(i,j),num)
                    if len(neighArr) == 0: errorStr += "ERROR 3"
                    if len(neighArr) == 1:
                        nR,nC = neighArr[0]
                        if num not in potArr[(nR,nC)]: errorStr += "SERIOUS ERROR"
                        potArr[(nR,nC)] = [num]
                        potArr = removeDups(potArr)

        for key,item in potArr.items():
            if len(item) == 1:
                r,c = key
                x = item[0]
                if grid[r][c] == 0:
                    grid[r][c] = x

    dictPrint(potArr,grid)
    if errorStr != "": print("@@@@@@@@@@@@@@@@@@@@@ERRORS:", errorStr)
    return grid

def removeDups(potArr):
    grps = getParams()
    boolW = True
    while boolW:
        boolW = False
        for i in range(9):
            for j in range(9):
                if len(potArr[(i,j)]) == 1:
                    tgt = potArr[(i,j)][0]
                    for grp in grps:
                        if (i,j) in grp:
                            for coord in grp:
                                if tgt in potArr[coord] and coord != (i,j):
                                    potArr[coord].remove(tgt)
                                    if len(potArr[coord]) == 1: boolW = True
                            break
    return potArr

def dictPrint(potArr,grid):
    grps = getParams()
    counter = 0
    for key, item in potArr.items():
#    for key, item in sorted(potArr.items(), key = lambda k:(-len(k[1]))):
        if len(item) == 1: counter += 1
        if len(item)==2:
            print("{}: {}".format(key, item))
    idx = 0
    for grp in grps:
        idx +=1
        for num in range(1,9):
            counterX = 0
            temp = []
            for c in grp:
                if num in potArr[c]: 
                    counterX += 1
                    temp.append(c)
            if counterX == 2:
                print(num,temp)
            
#        print("Group",idx,":")
#        for e in grp:
#            print("{}: {}".format(e, potArr[e]))
    print("Grid Count: ",counter)
    strr = (8,6)
    print("X",strr,potArr[strr])

def getSuperNeigh(potArr,coord,x):
    r,c = coord
    grps = getParams()
    ans = []
    if r-x >= 0: ans.append((r-x,c))
    if r+x <= 8: ans.append((r+x,c))
    if c-x >= 0: ans.append((r,c-x))
    if c+x <= 8: ans.append((r,c+x))
    tempAns = dc(ans)
    for tR,tC in ans:
        if x not in potArr[(tR,tC)]: tempAns.remove((tR,tC))
    ans = tempAns
    for grp in grps:
        if coord in grp:
            temp = dc(ans)
            for neigh in ans:
                if neigh in grp: temp.remove(neigh)
            return temp
    return "error"

start = time.time()
y = getGrid()
y = jamGrid(y)
y[0][2] = 8
y[1][3] = 7
y[2][8] = 6
y[1][5] = 6
y[3][2] = 5
#y[0][3] = 1
finalGrid = getAllpot(y,5)
print("RESULT",verifyGrid(finalGrid),"!")
printer(finalGrid)
end = time.time()
print("Time Taken: ",end - start)
