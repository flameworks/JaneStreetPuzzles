from basic import getParams, printer, getGrid, verifyGrid, scorer, getGrpNum, getSuperNeigh
from dictMethods import dictPrint, dictFixedCount
import time

def getAllPotentials(grid,itier):
    grps = getParams()
    potArr = {}
    errorStr = ""
    prevCount = 0
    # Fill array dict of potential values per cell
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0: potArr[(i,j)]= list(range(1,len(grps[getGrpNum((i,j),grps)])+1))
            else:potArr[(i,j)]= [grid[i][j]]

    # Iterative section starts
    itiCounter = 0
    while True:
        itiCounter += 1        
        # Switch 'while' state if grid filling is stagnant.
        gridCount = dictFixedCount(potArr)
        if gridCount == prevCount: break
        prevCount = gridCount 

        for i in range(9):
            for j in range(9):
                # Remove options from cells that dont have available spatial neighbours.
                if len(potArr[(i,j)]) > 1:
                    for pot in potArr[(i,j)]:
                        neighArr = getSuperNeigh(potArr,(i,j),pot)
                        if len(neighArr) == 0: potArr[(i,j)].remove(pot)
                    if len(potArr[(i,j)]) == 0: errorStr += "ERROR 1"
                elif len(potArr[(i,j)]) == 0: errorStr += "ERROR 2"
                            
                # For fixed cells
                if len(potArr[(i,j)]) == 1:
                    # Because cell is fixed, remove this option from cage-mates. 
                    tgt = potArr[(i,j)][0]
                    grp = grps[getGrpNum((i,j),grps)]
                    for coord in grp:
                        if tgt in potArr[coord] and coord != (i,j):
                            potArr[coord].remove(tgt)      
                    # If fixed cell has a singleton spatial neighbour, fix neighbour.
                    num = potArr[(i,j)][0]
                    neighArr = getSuperNeigh(potArr,(i,j),num)
                    if len(neighArr) == 0: errorStr += "ERROR 3"
                    if len(neighArr) == 1:
                        nR,nC = neighArr[0]
                        if num not in potArr[(nR,nC)]: errorStr += "SERIOUS ERROR"
                        potArr[(nR,nC)].clear()
                        potArr[(nR,nC)].append(num)
        
        # Fix cells that requires a specific number has to be filled due to cage restrictions.
        for grp in grps:
            temp = []
            for coord in grp:
                temp += potArr[coord]
            for num in range(1,9):
                if temp.count(num) == 1:
                    for coord in grp:
                        if num in potArr[coord]:
                            r,c = coord
                            potArr[(r,c)].clear()
                            potArr[(r,c)].append(num)
                            break

    for key,item in potArr.items():
        if len(item) == 1:
            r,c = key
            x = item[0]
            if grid[r][c] == 0:
                grid[r][c] = x
                
    dictPrint(potArr,grid)
    if errorStr != "": print("@@@@@@@@@@@@@@@@@@@@@ERRORS:", errorStr)
    print("Iterations: ",itiCounter)
    return grid

start = time.time()
y = getGrid()
y[0][2] = 8
y[1][3] = 7
y[7][5] = 6
y[3][2] = 5
y[2][8] = 6
y[1][5] = 6
y[2][4] = 3
finalGrid = getAllPotentials(y,5)
print("RESULT",verifyGrid(finalGrid),"!")
printer(finalGrid)
print("SCORE: ",scorer(finalGrid))
end = time.time()
print("Time Taken: ",end - start)
