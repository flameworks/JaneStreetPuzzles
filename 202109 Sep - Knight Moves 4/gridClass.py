from methods import *

class gridObj:
    iteration = 0
    def __init__(self, testCase, LIMIT = 0):
        self.idx, self.arr, self.key, self.area, \
            self.areaGrid, self.maxNum, self.areaNum, \
                self.loc, self.areaLoc, self.sectSums = getArr(testCase)
        
        sumLimit = LIMIT*(LIMIT+1)/2/len(self.area)
        if sumLimit == int(sumLimit): self.sumLimit = sumLimit
        else: self.sumLimit = False
        
        self.restrict = self.getRestrictions()
        
    ###### Grid Moves ######
    def getPossible(self, prevAdd):
        if prevAdd in self.loc:
            return prevAdd+1, getKnightMoves(self.loc[prevAdd], self.idx)
        return (1, sorted(self.restrict[1]))

    def add(self,num,coord):
        x,y = coord
        if self.arr[x][y] == num: return True
        if num in self.loc: return False
        if self.arr[x][y] != 0: return False
        if self.restrict[num]:
            if coord not in self.restrict[num]: return False
        if self.sectSums[ self.areaLoc[(x,y)] ] + num > self.sumLimit:
            return False
        self.arr[x][y] = num
        self.sectSums[ self.areaLoc[(x,y)] ] += num
        self.loc[num] = (x,y)
        for sectSum in self.sectSums:
            if sectSum > self.sumLimit: return self.remove(num,coord)
            if 0 < self.sumLimit-sectSum < num+1: return self.remove(num,coord)
        return True

    def remove(self,num,coord):
        if coord in self.key: return False
        x,y = coord
        self.arr[x][y] = 0
        self.loc.pop(num)
        self.sectSums[ self.areaLoc[coord] ] -= num
        return False
        
    ###### Grid Methods ######
    def getRestrictions(self):
        restrict = [ set() for i in range(self.idx**2+1)]
        for coord in self.key:
            x,y = coord
            num = self.arr[x][y]
            restrict[num-1] = set(getKnightMoves(coord,self.idx))
            restrict[num] = set([coord])
            restrict[num+1] = set(getKnightMoves(coord,self.idx))
        for idx, sets in enumerate(restrict):
            if idx < 2: continue
            temp = []
            if idx > self.maxNum: break
            if len(sets):
                for coord in sets:
                    temp+= getKnightMoves(coord,self.idx)
                temp = set(temp)
                if len(restrict[idx-1]):
                    restrict[idx-1] = restrict[idx-1].intersection(temp)
                else:
                    restrict[idx-1] = temp
                if idx+1 < self.idx**2:
                    if len(restrict[idx+1]):
                        restrict[idx+1] = restrict[idx+1].intersection(temp)
                    else:
                        restrict[idx+1] = temp
        return restrict
                
    def scorer(self):
        ans = 0
        strr = ''
        strr2 = ''
        for row in self.arr:
            ans += (max(row))**2
            strr += f'{max(row)}^2 + '
            strr2 += f'{max(row)**2} + '
##        print(strr[:-2], f'= {ans:,}')
##        print(strr2[:-2], f'= {ans:,}')
        return ans

    ###### Verification ######    
    def verify(self):
        return len(set(self.sectSums)) == 1
    
    ###### Prints ######
    def pprint(self, areaBool = False, stepNum = None):
        if areaBool: arr = self.areaGrid
        else: arr = self.arr
        topLine = '   '
        for i in range(self.idx):
            topLine += str(i)+'  '
        print(topLine)
        for cnt in range(self.idx):
            row = arr[cnt]
            strr = str(cnt) + "|"
            for i in range(self.idx):
                if stepNum != None and self.areaGrid[cnt][i] != stepNum:
                    strr += "  "
                else:
                    if row[i] <= 0: strr += " "
                    if row[i] < 10: strr += " "
                    if row[i] > 0: strr += str(row[i])
                if i < self.idx-1: strr += "|"
            strr += "|" + str(cnt)
            print(strr)
        botLine = '   '
        for i in range(self.idx):
            botLine += str(i)+'  '
        print(botLine)
        print()
