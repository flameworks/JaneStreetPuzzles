import time
import random
import math as m

def main():
    for k in range(1,20):
        D = 1.03
        angle = 0
        for i in range(1000000):
            angle += tttt(D)
        print(D, angle / 1000000 / 360)
    return 0
        
def tttt(D):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if D == None: D = random.uniform(0,1)
    cArr = getC(x,y,D)
    gdAngle = 0
    badAngle = 0
    for idx in range(len(cArr)):
        c1 = cArr[idx-1]
        c2 = cArr[idx]
        base = getDist(c1,c2)
        if boolIntersect(c1,c2): gdAngle += getAngle(base,D)
        if len(cArr) == 2: break
    badAngle = 360 - gdAngle  
    return gdAngle
    
def getDist(c1,c2):
    x1,y1 = c1
    x2,y2 = c2  
    dist = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return dist  

def getAngle(base,D):
    return m.degrees(m.acos( (D**2 + D**2 - base**2) / (2*D*D)))

def boolIntersect(c1,c2):
    x1,y1 = c1
    x2,y2 = c2
    midPt = ( (x1+x2)/2, (y1+y2)/2 )

    x,y = midPt
    if (x <= 0 or x >= 1) and (y > 0 and y < 1): return True
    if x < 1 and (y >= 1 or y <= 0): return True
    return False
    
def getC(x,y,D):
    (x1,y1), (x4,y4) = roots(D, 1-y, x, 1)
    (x8,y8), (x5,y5) = roots(D, y, x, 0)
    (x7,y7), (x2,y2) = coordFlip(roots(D, x, y, 0))
    (x6,y6), (x3,y3) = coordFlip(roots(D, 1-x, y, 1))
    cArr = [(x1,y1),(x2,y2),(x3,y3),(x4,y4), \
            (x5,y5),(x6,y6),(x7,y7),(x8,y8)]
    upper = [];    lower = []
    for i,j in cArr:
        if i == None: continue
        if j > y: upper.append((i,j))
        else: lower.append((i,j))
    upper.sort()
    lower.sort()
    lower.reverse()
    return upper + lower

def roots(D, h, bCoord,bH):
    discri = D**2 - (h)**2
    if discri <= 0: return ((None,None),(None,None))
    leng = discri ** 0.5
    c1 = (bCoord - leng , bH)
    c2 = (bCoord + leng , bH)
    return (c1,c2)

def coordFlip(coord):
    c1,c2 = coord
    x,y = c1
    a,b = c2
    return( (y,x), (b,a) )

start = time.time()
x = main()
end = time.time()
print("Time Taken: ",end - start)    

'''
A random line segment of length D is chosen on a plane marked
with an infinite checkerboard grid (i.e., a unit side length
square grid).  What length D maximizes the probability that
the segment crosses exactly one line on the checkerboard grid,
and what is this maximal probability?
'''
