import time
from basicOct import getGrid, printer, scorer
from hashPole import getHash, getHashAns

def main():
    start = time.time()
    g = getGrid()
    # PoleArr customised pole selections for speed
    # Manual trials needed and done to reduce combinational fanout
    poleArr = [(0,13),(1,14),(3,16),(6,16),(10,15),(4,13),
               (2,12),(6,11),(15,2),(10,0),(13,0),(16,3),
               (6,1),(2,0),(1,3),(5,2),(0,9),(2,5),(4,7),
               (8,8),(10,5),(12,3),(12,9),(11,14),
               (14,4),(16,7),(14,11),(15,13),(14,16)]

#    globHash = getHash() # 3.52 Sec
    globHash = getHashAns() # Shortened result from hashPole.py to get all triangle combinations
    print("Hash: ",time.time() - start)
    start = time.time()    
    
    finalRoute = [];    routeArr = []
    endRouteLen = len(poleArr)
    routeArr.append( [] )
    cnt = 0
    for i,j in poleArr:
        print((i,j),g[i][j],"Len",len(routeArr),"Time:",time.time() - start)
        start = time.time()
        poleCoord = (i,j)
        fixedLen = len(routeArr)
        for idx in range(fixedLen):
            triArr = routeArr[idx]
            potentialTri = globHash[poleCoord]
            for tri1 in potentialTri:
                flag = False
                for tri in triArr:
                    cnt += 1
                    if tri_intersect2(tri, tri1):
                        flag = True
                        break
                if flag: continue
                newTriArr = triArr + [tri1]
                if len(newTriArr) == endRouteLen:
                    finalRoute.append(newTriArr)               
                else:
                    routeArr.append(newTriArr)
        routeArr = routeArr[fixedLen:]
    print()
    print("1 Unique Ans? >",len(finalRoute)==1,",",len(finalRoute))
    print("Triangle Comparisons:",'{:,}'.format(cnt))
    return finalRoute
    

def line_intersect2(v1,v2,v3,v4):
#    judge if line (v1,v2) intersects with line(v3,v4)
    d = (v4[1]-v3[1])*(v2[0]-v1[0])-(v4[0]-v3[0])*(v2[1]-v1[1])
    u = (v4[0]-v3[0])*(v1[1]-v3[1])-(v4[1]-v3[1])*(v1[0]-v3[0])
    v = (v2[0]-v1[0])*(v1[1]-v3[1])-(v2[1]-v1[1])*(v1[0]-v3[0])
    if d<0: u,v,d = -u,-v,-d
    return (0< u < d) and (0 < v < d)

def tri_intersect2(t1, t2):
#    judge if two triangles in a plane intersect 
    if line_intersect2(t1[0],t1[1],t2[0],t2[1]): return True
    if line_intersect2(t1[0],t1[1],t2[0],t2[2]): return True
    if line_intersect2(t1[0],t1[1],t2[1],t2[2]): return True
    if line_intersect2(t1[0],t1[2],t2[0],t2[1]): return True
    if line_intersect2(t1[0],t1[2],t2[0],t2[2]): return True
    if line_intersect2(t1[0],t1[2],t2[1],t2[2]): return True
    if line_intersect2(t1[1],t1[2],t2[0],t2[1]): return True
    if line_intersect2(t1[1],t1[2],t2[0],t2[2]): return True
    if line_intersect2(t1[1],t1[2],t2[1],t2[2]): return True
    return False

printer(getGrid())
start = time.time()
x = main()
finalRoute = x[0]
print("Score:",'{:,}'.format(scorer(finalRoute)))
end = time.time()
print("Time Taken: ",end - start)    

