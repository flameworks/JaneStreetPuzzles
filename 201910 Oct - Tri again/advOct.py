import time
from copy import deepcopy as dc, copy
from basicOct import getGrid, printer
from hashPole import xx
from statistics import mean

def main():
    g = getGrid()
    globHash = xx()
    finalRoute = []
    routeArr = []  #[ [pole1,pole2..], [tri1,tri2..], [blockedPts]  ]
    poleCoordArr = []
    for i in range(17):
        for j in range(17):    
            pole = g[i][j]
            poleCoord = (i,j)   
            if pole == 0: continue            
            poleCoordArr.append([pole,poleCoord])
        
    pole = g[1][14]
    poleCoord = (1,14)
    potentialTri = globHash[poleCoord]    
    for base,h,v in potentialTri:
        intPts, filledSq = getInteriorPts(base, h, v)
        routeArr.append([[poleCoord],[(base,h,v)],copy(intPts)])  
    
    poleArr = [(4,13),(3,16),(2,12)]
    while routeArr:
        route, triArr, blockedPts = routeArr.pop()
#        print(len(routeArr),len(route),route)
        if len(route) == len(poleArr)+1:
            finalRoute.append([route, triArr, blockedPts])
#            print(finalRoute)
#            return g
            continue
        for i,j in poleArr:
            pole = g[i][j]
            poleCoord = (i,j)
            if pole == 0: continue
            if poleCoord in route: continue
            potentialTri = globHash[poleCoord]
            for base,h,v in potentialTri:
                intPts, filledSq = getInteriorPts(base, h, v)
                outSq = getStepLadder(base, h, v)
                flag = True
                for innerPt in intPts:
                    if innerPt in blockedPts:
                        flag = False
                        break
                if flag:
                    newRoute = copy(route) + [poleCoord]
                    newTriArr = copy(triArr) + [(base,h,v)]
                    newBlocked = copy(intPts)
                    for pt in blockedPts:
                        newBlocked.append(pt)
                    routeArr.append([newRoute,newTriArr,newBlocked])
    print(len(finalRoute))
#    print(finalRoute[1500][0])
#    print(finalRoute[1500][1])
#    print(finalRoute[1500][2])
    return g

def getHash():
    g = getGrid()
    globHash = {}
    for b1 in range(0,1): # Edges use range 18
        for b2 in range(12,15): # Edges use range 18
            print(b1,b2)
            base = (b1,b2)
            for h2 in range(18):
                for v1 in range(18):
                    h = (b1,h2);    v = (v1,b2)
                    intPts, filledSq = getInteriorPts(base, h, v)
                    outSq = getStepLadder(base, h, v)
                    counter = 0; counter2= 0; val = -1;   valR = -1; valC = -1
                    for r,c in filledSq:
                        if g[r][c] != 0: 
                            counter += 1
                            val = g[r][c]; valR = r; valC = c
                        if counter > 1: break
                    for r,c in outSq:
                        if g[r][c] != 0: counter2 += 1
                        if counter2 > 1: break           
                    if counter == 1 and counter2 == 1:
                        area = getArea(base,h,v)
                        if area == val:
                            if (valR,valC) in globHash:
                                globHash[(valR,valC)].append((base,h,v))
                            else:
                                globHash[(valR,valC)] = [(base,h,v)]
#    print(globHash[(15,2)])
    print(globHash)
    print("Length",len(list(globHash.keys())))
    return g

def getStepLadder(base, h, v):
    b1,b2 = base; h1,h2 = h; v1,v2 = v
    newBase = (v1,h2)
    newInt,newFill = getInteriorPts(newBase, v, h)
    top1 = min(v1,b1);    top2 = min(h2,b2)
    bot1 = max(v1,b1);    bot2 = max(h2,b2)
    totalAns = []
    for i in range(top1,bot1):
        for j in range(top2,bot2):
            totalAns.append((i,j))
    for coord in newFill:
        totalAns.remove(coord)
    return totalAns

def getInteriorPts(base, h, v): # Base, HORI, VERT
    b1,b2 = base; h1,h2 = h; v1,v2 = v
    cMain = max(b1,h1,v1,b2,h2,v2)
    intPts = []
    for x1 in range(cMain):
        for x2 in range(cMain):
            i = x1 ; j = x2 # VERY BAD NOT FINDING DIRECTION @@@@@@@@@@@@@@@@
            if ptInTriangle((i,j), base, h, v): intPts.append((i,j))
#    return intPts
    filledSq = [] # Area 2 issue
    for r,c in intPts:
        newR = -1; newC = -1
        if h2 > b2: newC = c-1
        if h2 < b2: newC = c
        if v1 > b1: newR = r-1
        if v1 < b1: newR = r
        filledSq.append((newR,newC))
    if abs(h2-b2) == 2 and abs(v1-b1) == 2:
        top1 = min(v1,b1);    top2 = min(h2,b2)
        bot1 = max(v1,b1);    bot2 = max(h2,b2)
        midPt = (mean([top1,bot1]),mean([top2,bot2]))
        r,c = midPt
        if h2 > b2: newC = c-1
        if h2 < b2: newC = c
        if v1 > b1: newR = r-1
        if v1 < b1: newR = r      
        filledSq.append((newR,newC))
    return [intPts,filledSq]

def ptInTriangle(p, p0, p1, p2): # Not specific
    A = 1/2 * (-p1[0] * p2[1] + p0[0] * (-p1[1] + p2[1]) + p0[1] * (p1[0] - p2[0]) + p1[1] * p2[0])
    sign = 1
    if A < 0: sign = -1
    s = (p0[0] * p2[1] - p0[1] * p2[0] + (p2[0] - p0[0]) * p[1] + (p0[1] - p2[1]) * p[0]) * sign
    t = (p0[1] * p1[0] - p0[0] * p1[1] + (p0[0] - p1[0]) * p[1] + (p1[1] - p0[1]) * p[0]) * sign
    return s > 0 and t > 0 and (s + t) < 2 * A * sign

def getArea(base,h,v): # Only base specific
    b1,b2 = base;   h1,h2 = h;  v1,v2 = v    
    height = abs(v1-b1)
    length = abs(h2-b2)
    if height % 2 == 1 and length % 2 == 1: return False
    return 0.5 * height * length
    
#x = getHash()
    
start = time.time()
#x = main()
#printer(x)
end = time.time()
print("Time Taken: ",end - start)    

#    { (2, 0): [((2, 0), (2, 2), (6, 0)), 
#             ((2, 0), (2, 4), (4, 0))], 
#     (1, 3): [((2, 0), (2, 12), (0, 0)), 
#             ((2, 1), (2, 13), (0, 1)), 
#             ((2, 2), (2, 14), (0, 2))], 
#     (2, 5): [((2, 2), (2, 12), (4, 2))]}
#
#printer(getGrid())
tri = ( (1, 17), (1, 10), (3, 17)  )
print("Step Ladder",getStepLadder( tri[0],tri[1],tri[2] ))
print("Int Pts",getInteriorPts(tri[0],tri[1],tri[2] )[0])
print("Int Unit",getInteriorPts( tri[0],tri[1],tri[2])[1])

#print(getArea( (4,5),(4,0),(0,5) ))
#print( ptInTriangle((1,2), (3,0),(0,4),(0,0) ) )
#print(getInteriorPts((4,5),(4,0),(0,5) ))
