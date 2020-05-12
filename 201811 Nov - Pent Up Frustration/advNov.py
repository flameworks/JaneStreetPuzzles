import time
from basicNov import printer, getGrps, getGrid, getPosGrid, \
getNeigh, getPotentials, scorer, verifyCounts

def main():
    matrix = getGrid()
    params = getGrps()
    potenHash = getPotentials()
    print("Searching...")
    if solveGrid(matrix,params,potenHash):
        print("Smallest Product:", scorer(matrix))
        printer(matrix)
    else:
        print("No solution")
    return matrix
    
def solveGrid(matrix,params,potenHash):
    r, c, countMatrixNums = getNextCoord(matrix)
    if r == -1: return True
    cToGrp, grpToC = params
    grpNum = cToGrp[(r,c)]
    ownGrp = grpToC[grpNum]
    temp = [0,0]
    for n1,n2 in ownGrp:
        if n1 == r and n2 == c: continue
        n = matrix[n1][n2]
        if n != 1: 
            if temp[0] != 0: temp[1] = n
            else: temp[0] = n
    potentialNums = potenHash[tuple(temp)]
    for num in potentialNums:
        if countMatrixNums[num] >= 7: return False
        if gridPlacementCheck(num, r, c,matrix,ownGrp):
            matrix[r][c] = num
            if solveGrid(matrix,params,potenHash): return True
            matrix[r][c]=0
    return False
    
def getNextCoord(matrix):
    glob = [0]*21
    for i in range(7):
        for j in range (7):
            num = matrix[i][j]
            glob[num] += 1
            if num == 0: return (i, j, glob)
    return (-1,-1, glob)

def gridPlacementCheck(num, r, c, matrix,ownGrp):
    if num >= 8:
        neigh = getNeigh((r,c))
        for n1,n2 in neigh:
            if matrix[n1][n2] >= 8: return False        
    for i in range(7): 
        if matrix[r][i] == num: return False # Same col
        if matrix[i][c] == num: return False # Same row 
    for n1,n2 in ownGrp: # Same Grp
        if matrix[n1][n2] == num: return False
    return True

start = time.time()
x = main()
print("Validity",verifyCounts(x))
print("Grps:")
printer(getPosGrid())
end = time.time()
print("Time Taken: ",end - start)    

'''
Fill each cell with a positive integer such 
that integers do not repeat within any row, column,
 or outlined region. Within each region, one cell 
 must be equal to the product of the other cells, 
 and these “product” cells may not share edges with
 “product” cells from other regions. (See the example.)

The answer to this month’s puzzle is the smallest possible sum for the “product” cells.

Please send in your answer, as well as your grid.
(E.g., the first row of the filled-out Example would read “3,6,4,2”.)
'''
