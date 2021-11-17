import math

numHash = {}
for i in range(1,10):
    for j in range(1,10):
        c = math.gcd(i,j)
        if c > 1:
            if c in numHash:
                numHash[c].append(i)
                numHash[c].append(j)
            else: numHash[c] = [i, j]

for x in numHash:
    numHash[x] = list(set(numHash[x]))

def verify(num, grid):
    if len(grid) != len(str(num)): return False
    for idx, c in enumerate(grid):
        if c == 'x': continue
        d = int(str(num)[idx])
        if d not in numHash[int(c)]: return False
    return True
