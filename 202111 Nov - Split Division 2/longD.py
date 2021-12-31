import math

class division:
    def __init__(self, dividend, divisor):
        self.num = dividend
        self.divisor = divisor
        self.ans = dividend//divisor
        self.numA = self.splitNum(dividend)
        self.divA = self.splitNum(divisor)
        self.ansA = self.splitNum(dividend//divisor)
        self.lineA = []
        self.divide()

    def splitNum(self, num):
        ans = []
        for c in str(num):
            ans.append(int(c))
        return ans

    def joinNum(self,arr):
        strr = ''
        for c in arr:
            strr+= str(c)
        if len(strr): return int(strr)
        else: return False

    def quickDiv(self, dividend, divisor):
        quotient = dividend // divisor
        return (quotient, quotient * divisor)
        
    def divide(self):
        for idx in range(1,len(self.numA)):
            nxtNum = self.joinNum(self.numA[:idx])
            if nxtNum > self.divisor: break
            
        for N in self.ansA:
            currNum = N * self.divisor
            self.lineA.append(currNum)
            nxtNum = nxtNum - currNum
            if idx < len(self.numA):
                nxtNum = nxtNum * 10 + self.numA[idx]
            idx += 1
            self.lineA.append(nxtNum)

    def compare(self, divObj, gridArr):
        compareArr = [self.divisor, self.ans, self.num] + self.lineA
        compareArr2 = [divObj.divisor, divObj.ans, divObj.num] + divObj.lineA
        
        for POS in range(len(compareArr)):
            num1 = str(compareArr[POS])
            num2 = str(compareArr2[POS])
            grid = gridArr[POS]

            for idx, c1 in enumerate(num1):
                c1 = int(c1)
                c2 = int(num2[idx])
                g = grid[idx]
                if g == 'x': g = 1
                if c1 == 0 or c2 == 0: continue
                if math.gcd(c1,c2) != int(g): return False
        return True
        
    def pprint(self):
        print(self.num, self.divisor, self.joinNum(self.ansA))
        for x in self.lineA:
            print(x)

