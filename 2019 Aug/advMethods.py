from baseMethods import viewer, getParams

def verifyGrid(grid):
    params = getParams()
    for j in range(8):
        for i in range(4):
            if viewer(grid,i,j) != params[i][j] and params[i][j] != 0: return False
    return True

def placementBool(rx,cx,nxtInput,tempGrid2):
    top,rhs,bot,lhs = getParams()
    if rx == 0 and nxtInput != top[cx] and top[cx] != 0: return True
    if cx == 0 and nxtInput != lhs[rx] and lhs[rx] != 0: return True
    if rx == 7 and nxtInput != bot[cx] and bot[cx] != 0: return True
    if cx == 7 and nxtInput != rhs[rx] and rhs[rx] != 0: return True

    if nxtInput in top and cx != top.index(nxtInput): return True
    if nxtInput in rhs and rx != rhs.index(nxtInput): return True
    if nxtInput in bot and cx != bot.index(nxtInput): return True
    if nxtInput in lhs and rx != lhs.index(nxtInput): return True

    if nxtInput in top:
        for i in range(0,rx):
            if tempGrid2[i][cx] > 0: return True
            tempGrid2[i][cx] = 0
    if nxtInput in rhs:
        for i in range(cx+1,8):
            if tempGrid2[rx][i] > 0: return True
            tempGrid2[rx][i] = 0
    if nxtInput in bot:
        for i in range(rx+1,8):
            if tempGrid2[i][cx] > 0: return True
            tempGrid2[i][cx] = 0
    if nxtInput in lhs:
        for i in range(0,cx):
            if tempGrid2[rx][i] > 0: return True
            tempGrid2[rx][i] = 0
    return False
