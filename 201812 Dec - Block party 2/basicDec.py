from copy import copy as c
def getPotentials():
    lists = [[4,5,20],[3,5,15],[2,6,12],[3,4,12],[2,5,10],[2,4,8]]        
    glob = {}
    for n1 in range(2,21):
        for n2 in range(n1+1,21):
            for tup in lists:
                if n1 in tup and n2 in tup:
                    glob[(n1,n2)] = c(tup)
                    glob[(n1,n2)].remove(n1)
                    glob[(n1,n2)].remove(n2)
    for tup in lists:
        for x in tup:
            if (x,0) not in glob:
                glob[(x,0)] = c(tup)
            else:
                glob[(x,0)] += c(tup)
            glob[(x,0)].remove(x)
    tempKeys = []
    for x in glob:
        tempKeys.append(x)
        glob[x] = tuple(set(glob[x]))
    for n1,n2 in tempKeys:
        if (n2,n1) not in glob: glob[(n2,n1)] = glob[(n1,n2)]
    glob[(0,0)] = (2,3,4,5,6,8,10,12,15,20)
    return glob

def verifyCounts(matrix):
    glob = countMatrix(matrix)
    for x in glob:
        if glob[x] > 7: return False
    return True

def countMatrix(matrix):
    glob = [0]*21
    for i in range(7):
        for j in range(7):
            num = matrix[i][j]
            glob[num] += 1
    return glob

def scorer(m):
    ans = 0
    for i in range(7):
        for j in range(7):
            if m[i][j] >= 8: ans += m[i][j]
    return ans
def getGrid():
    y = [None] * 7
    for i in range(7):
        y[i] = [0] * 7
    y[5][3] = 1 # (16s)
#    y[6][4] = 1 # Uncomment this and comment above for the solution presented (106s)
    return y


def getNeigh(coord):
    r1,c1 = coord
    neigh = []
    if r1 > 0: neigh.append((r1-1,c1))
    if r1 < 6: neigh.append((r1+1,c1))
    if c1 > 0: neigh.append((r1,c1-1))
    if c1 < 6: neigh.append((r1,c1+1))
    return neigh

def printer(y):
    print("   0  1  2  3  4  5  6 ")
    for cnt in range(7):
        row = y[cnt]
        strr = str(cnt) + "|"
        for i in range(7):
            if row[i] <= 0: strr += " "
            if row[i] < 10: strr += " "
            if row[i] > 0: strr += str(row[i])
            if i < 6: strr += "|"
        strr += "|" + str(cnt)
        print(strr)
    print("   0  1  2  3  4  5  6 ")

def getGrps():
    y = getPosGrid()
    cToGrp = {}; grpToC = {}
    for i in range(7):
        for j in range(7):
            pole = y[i][j]
            cToGrp[(i,j)] = pole
            if pole not in grpToC:
                grpToC[pole] = [(i,j)]
            else:
                grpToC[pole].append((i,j))
    return [cToGrp,grpToC]

def getPosGrid():
    y = [None] * 7
    y[0] = [1,2,2,3,3,4,4]
    y[1] = [1,1,2,5,3,4,6]
    y[2] = [7,7,5,5,8,6,6]
    y[3] = [9,7,10,10,8,8,11]
    y[4] = [9,9,12,10,13,11,11]
    y[5] = [14,12,12,15,13,13,0]
    y[6] = [14,14,15,15,15,0,0]
    return y

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
