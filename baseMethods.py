from numpy import prod
import heapq as h
import copy

def scorer(g,b):
    grid = copy.deepcopy(g)
    score = []
    for r in range(8):
       for c in range(8):
           if grid[r][c] <= 0:
               temp = [[r,c]]
               tempScore = 1
               grid[r][c] = 1000
               while temp:
                   rx,cx = h.heappop(temp)
                   for nr,nc in traverse(rx,cx):
                       if grid[nr][nc] <= 0:
                           tempScore += 1
                           h.heappush(temp,[nr,nc])
                           grid[nr][nc] = 1000
               score.append(tempScore)
    if b: print("ScoreArr: ",score)
    return prod(score)

def traverse(r,c):
    ans = []
    if r >= 1: ans.append([r-1,c])
    if c >= 1: ans.append([r,c-1])
    if r <= 6: ans.append([r+1,c])
    if c <= 6: ans.append([r,c+1])
    return ans

def horseMoves(r,c):
    ans = []
    if r >= 2 and c >= 1: ans.append([r-2,c-1])
    if r >= 2 and c <= 6: ans.append([r-2,c+1])
    if r <= 5 and c >= 1: ans.append([r+2,c-1])
    if r <= 5 and c <= 6: ans.append([r+2,c+1])
    if r >= 1 and c >= 2: ans.append([r-1,c-2])
    if r <= 6 and c >= 2: ans.append([r+1,c-2])
    if r >= 1 and c <= 5: ans.append([r-1,c+2])
    if r <= 6 and c <= 5: ans.append([r+1,c+2])
    return ans

def printer(y):
    print("   0  1  2  3  4  5  6  7  ")
    for cnt in range(8):
        row = y[cnt]
        strr = str(cnt) + "|"
        for i in range(8):
            if row[i] <= 0: strr += " "
            if row[i] < 10: strr += " "
            if row[i] > 0: strr += str(row[i])
            if i < 7: strr += "|"
        strr += "|" + str(cnt)
        print(strr)
    print("   0  1  2  3  4  5  6  7  ")

def viewer(grid,direction,idx):
    if direction == 0:
        for row in grid:
            if row[idx] != 0: return row[idx]
    elif direction == 1:
        for i in range(7,-1,-1):
            if grid[idx][i] != 0: return grid[idx][i]
    elif direction == 2:
        for i in range(7,-1,-1):
            if grid[i][idx] != 0: return grid[i][idx]
    elif direction == 3:
        for i in range(7):
            if grid[idx][i] != 0: return grid[idx][i]

def getGrid():
    y = [None] * 8
    for i in range(8):
        y[i] = [-1] * 8
    return y

def getParams():
    top = [0,29,19,33,20,27,36,35]
    rhs = [0,26,36,25,37,4,23,6]
    bot = [13,14,12,2,1,5,7,0]
    lhs = [18,19,30,10,16,11,12,0]
    return [top,rhs,bot,lhs]
