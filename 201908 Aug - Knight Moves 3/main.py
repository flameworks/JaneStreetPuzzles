from heapq import heappush as hpush, heappop as hpop, heapify
from copy import deepcopy as dc
from baseMethods import printer, horseMoves, scorer, getGrid
import time
from advMethods import placementBool, verifyGrid

def main():
    ans, workingList = [], []
    for i in range(8):
        newGrid = getGrid()
        newGrid[i][4] = 1
        for k in range(i+1,8): newGrid[k][4] = 0
        hpush(workingList,[-1,newGrid,i,4,2])
    while workingList:
        s,tempGrid,lastR,lastC,nxtInput = hpop(workingList)
        flag = True
        for rx,cx in horseMoves(lastR,lastC):
            if tempGrid[rx][cx] == -1:
                tempGrid2 = dc(tempGrid)
                if placementBool(rx,cx,nxtInput,tempGrid2): continue
                flag = False
                tempGrid2[rx][cx] = nxtInput
                hpush(workingList,[-nxtInput,tempGrid2,rx,cx,nxtInput+1])
        if flag and verifyGrid(tempGrid):
            hpush(ans,[scorer(tempGrid,False),tempGrid,nxtInput-1])
            heapify(ans)
    print("Answers: ",len(ans))
    print("Outstanding work on: ",len(workingList))
    for i in range(1):
        s, g, n = hpop(ans)
        print("Score: " , scorer(g,True))
        print("Max: " , n)
        printer(g)
        print()

start = time.time()
main()
end = time.time()
print("Time Taken: ",end - start)
