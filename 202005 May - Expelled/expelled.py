class CompleteGrid:
    def __init__(self,row=9,col=18):
        self.r = max(3,row)
        self.c = max(18,self.r*2,col)
        self.structure = list(map(lambda x: [0]*self.c, range(self.r)))
        self.structure[0] = list(range(1,self.c+1))
        
    def pprint(self):
        for row in self.structure:
            strr = '  '
            for n in row:
                if n == 0: strr += f'- '
                else: strr += f'{n} '
                if n < 10: strr += ' '
            print(strr)
            
    def fill(self):
        for diagIdx,row in enumerate(self.structure[1:]):
            rowIdx = diagIdx + 1
            currentIdx = 0
            for c in range(1,diagIdx + 1):
                self.structure[rowIdx][currentIdx] = self.structure[rowIdx-1][diagIdx-c]
                self.structure[rowIdx][currentIdx+1] = self.structure[rowIdx-1][diagIdx+c]
                currentIdx += 2
            for x in range(currentIdx, self.c):
                self.structure[rowIdx][x] = self.structure[rowIdx-1][x] + 1
                    
    def checker(self):
        ans = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[4,6,2,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],[2,8,6,9,4,10,11,12,13,14,15,16,17,18,19,20,21,22],[9,10,6,11,8,12,2,13,14,15,16,17,18,19,20,21,22,23],[8,2,11,13,6,14,10,15,9,16,17,18,19,20,21,22,23,24],[14,15,6,9,13,16,11,17,2,18,8,19,20,21,22,23,24,25],[11,2,16,18,13,8,9,19,6,20,15,21,14,22,23,24,25,26]]
        for idx,row in enumerate(self.structure):
            if idx > 8: continue
            for idx2,c in enumerate(row):
                if idx2 > 17: continue
                if c != 0 and c != ans[idx][idx2]:
                    print(idx,idx2,c, ans[idx][idx2])
                    return False
        for r in self.structure:
            for n in r:
                if n <= 0: return "Contains some Zeroes"
        return True

    def diag(self):
        return list(map(lambda x: x[1][ x[0] ], enumerate(self.structure)))

a = CompleteGrid(800)
a.fill()
print("GRID Status is",a.checker())
##a.pprint()

x = a.diag()
for i in range(1,18):
    if i == 16: continue
    print(i,x.index(i)+1)





