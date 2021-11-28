from gridClass import gridObj
import time

def main():
    TESTCASE = 0 #0 for advanced 10x10
##    TESTCASE = 1 #1 for simple 5x5
    grid = gridObj(TESTCASE)
    grid.pprint()
    for LIMIT in range(grid.areaNum,90):
        grid = gridObj(TESTCASE, LIMIT)
        if not grid.sumLimit: continue
        if _rec(grid, LIMIT, 1):
            grid.pprint()
            print(f'COMPLETED with {grid.iteration} iterations, LIMIT {LIMIT}')
            print(f'Section Sum is: {grid.sumLimit}')
            print(f'SCORE is: {grid.scorer():,}')
            return
        print(f'LIMIT {LIMIT} failed with {grid.iteration} iterations')
    return grid

def _rec(grid, LIMIT, prevAdd):
    if prevAdd == LIMIT: return grid.verify()
    grid.iteration += 1
    toAdd, possibles = grid.getPossible(prevAdd)
    for coord in possibles:
        if grid.add(toAdd, coord):
            if _rec(grid, LIMIT, toAdd): return True
            grid.remove(toAdd, coord)
    return False
    
start = time.time()
main()
end = time.time()
print(f'Time Taken: {end - start:.5f} sec')




