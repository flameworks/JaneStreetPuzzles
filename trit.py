class t:
    def __init__(self,s = ''):
        self.s = str(s).upper()
        self.rs = self.s[::-1]
        self.d = self._toDec(self.s)
        
    def _toDec(self, s):
        rs = s[::-1]
        ans = 0
        for idx, c in enumerate(rs):
            if c == 'T': c = -1
            else: c = int(c)
            ans += c * 4**idx
        return ans

    def m(self, T): #Takes in trit type
        s1 = self.s
        s2 = T.s
        rs2 = s2[::-1]
        ans = '0'
        for idx in range(len(rs2)):
            c = rs2[idx]
            mult = self._m(s1,c)
            for iteration in range(idx):
                mult += '0'
            ans = self._a( mult , ans)
        return ans 

    def _m(self, s1, c): #Takes in trit type
        rs1 = s1[::-1]
        ans = ''
        carry = 0
        for idx in range(len(rs1)):
            c1 = rs1[idx]
            carry, toAdd = self.mT(c1,c,carry)
            ans += str(toAdd)
        return ans[::-1]

    def mT(self,c1,c,carry):
        if c1 == 'T': c1 = -1
        if c == 'T': c = -1
        if carry == 'T': carry = -1
        ans = int(c1) * int(c) + int(carry)

        if ans == 6: return (1, 2)
        if ans == 5: return (1, 1)
        if ans == 4: return (1, 0)
        if ans == 3: return (1, 'T')
        if ans == 2: return (0, 2)
        if ans == 1: return (0, 1)
        if ans == 0: return (0, 0)
        if ans == -1: return (0, 'T')
        if ans == -2: return ('T', 2)
        if ans == -3: return ('T', 1)
        if ans == -4: return ('T', 0)
        print("need more LA",ans)

    def _a(self, s1, s2): #Takes in trit type
        rs1 = s1[::-1]
        rs2 = s2[::-1]
        ans = ''
        carry = 0
        while len(rs1) < len(rs2): rs1 += '0'
        while len(rs2) < len(rs1): rs2 += '0'
        for idx in range(len(rs1)):
            c1 = rs1[idx]
            c2 = rs2[idx]
            carry, toAdd = self.aT(c1,c2,carry)
            ans += str(toAdd)
        return ans[::-1]

    def aT(self,c1,c2,c3):
        if c1 == 'T': c1 = -1
        if c2 == 'T': c2 = -1
        if c3 == 'T': c3 = -1
        ans = int(c1) + int(c2) + int(c3)

        if ans == 6: return (1, 2)
        if ans == 5: return (1, 1)
        if ans == 4: return (1, 0)
        if ans == 3: return (1, 'T')
        if ans == 2: return (0, 2)
        if ans == 1: return (0, 1)
        if ans == 0: return (0, 0)
        if ans == -1: return (0, 'T')
        if ans == -2: return ('T', 2)
        if ans == -3: return ('T', 1)
        if ans == -4: return ('T', 0)
        print("need more LA",ans)


def base_convert(m, balBool, boolT = False):
    i = m
    b = 4
    result = ''
    while i > 0:
        toAdd = i%b
        if toAdd == 3:
            result = 'T' + result
            i = i//b + 1
        else:
            if toAdd == 2:
                if not boolT: return '2'
            result = str(i % b) + result
            i = i // b
    if boolT:
        if balBool: print(m, 'in Balanced 4 is', result)
        else: print(m, 'in base 4 is', result)
    return result


def main():
    target = 524294
##    target = 8197
    searchNum = 5
    
    print(f'Searching up to {searchNum:,} combinations')
    base_convert(target,True,True)
    for num in range(50000000,searchNum):
        b4Ans = base_convert(num*target,True)
        if '2' not in b4Ans:
            b4Num = base_convert(num,True)
            if '2' not in b4Num:
                print('Answer:')
                print(f'B is {num:,}: {b4Num}')
                print(f'C is {num*target:,}: {b4Ans}')
                return b4Num


import time
tic = time.perf_counter()
main()
toc = time.perf_counter()
print(f'Completed in {toc - tic:0.5f}s')
print()


x = t('20011')
y = t('1111T01')
print()
print(f'{x.d:,}: {x.s}')
print(f'{y.d:,}: {y.s}')
z = t( base_convert(x.d*y.d,True,False))
print(f'{z.d:,}: {z.s}')


x = t('200011')
y = t('11111T001')
print()
print(f'{x.d:,}: {x.s}')
print(f'{y.d:,}: {y.s}')
z = t( base_convert(x.d*y.d,True,False))
print(f'{z.d:,}: {z.s}')


x = t('2000011')
y = t('111111T0001')
print()
print(f'{x.d:,}: {x.s}')
print(f'{y.d:,}: {y.s}')
z = t( base_convert(x.d*y.d,True,False))
print(f'{z.d:,}: {z.s}')


x = t('20000011')
y = t('1111111T00001')

print()
print(f'{x.d:,}: {x.s}')
print(f'{y.d:,}: {y.s}')
z = t( base_convert(x.d*y.d,True,False))
print(f'{z.d:,}: {z.s}')


x = t('200000011')
y = t('11111111T000001')
print()
print(f'{x.d:,}: {x.s}')
print(f'{y.d:,}: {y.s}')
z = t( base_convert(x.d*y.d,True,False))
print(f'{z.d:,}: {z.s}')


x = t('2000000011')
y = t('111111111T0000001')
print()
print(f'{x.d:,}: {x.s}')
print(f'{y.d:,}: {y.s}')
z = t( base_convert(x.d*y.d,True,False))
print(f'{z.d:,}: {z.s}')


x = t('20000000011')
y = t('1111111111T00000001')
print()
print(f'{x.d:,}: {x.s}')
print(f'{y.d:,}: {y.s}')
z = t( base_convert(x.d*y.d,True,False))
print(f'{z.d:,}: {z.s}')


print()
print()

b = t('1TTTTTTTTT1TTTTTT00T0000011')
a = t('111111111T0000001')

print(b.s)
print(a.s)
print(b.d/a.d)


'''
def gen(n,r): # Bad iteration
    if n:
        yield from gen(n-1, r + '2')
        yield from gen(n-1, r + 'T')
        yield from gen(n-1, r + '0')
        yield from gen(n-1, r + '1')
    else: yield r
    
def g(finder = -1):
    n = 2 #10
    a = list(gen(n,'1'))
##    cnt = 0
##    cnt2 = 0

    nums = {}
    for i in a:
        x = t(i)
##        if x.d < 0: cnt += 1
##        else: cnt2 += 1
        if x.d < 0: continue
        nums[x.d] = x.s
        if x.d == finder:
            print(x.s, 'is', finder)
            break
    return nums


print('Gen Trits')
allTrits = g()
print('Done')
A = t('0020202021') # 524294
##A = t('211') # 37
##A = t('2011') # 133
##A = t('0002022T') # 
##A = t('2T1')
print(A.d,"is",A.s)

for j in range(1,1000000):
    if j not in allTrits: continue
    B = t(allTrits[j])
    C = t(B.m(A))
    if '2' not in C.s:
        print("ANSWER", B.d, B.s, j, allTrits[j])
        print(A.m(B), C.d, C.s)
        break

print()
print()

x = t('2000000011')
y = t('1T1T1T1T1')
z = t(y.m(x))

print(x.d, x.s)
print(y.d, y.s)
print(z.d, z.s)
'''



'''
print(29, '2T1')
print(t('1100T').d, '1100T')
print(t('1TT').d, '1TT')
print()
print(t('11111T').d, '11111T')
print(t('1T0T').d, '1T0T')
print()
print(t('2000000011').d, '2000000011')

print(t('2T').d, '2T')
print(t('1T01').d, '1T01')


def base_convert(m, b, boolT):
    i = m
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b

    x = ''
    for j in result:
        x += str(j)
    if boolT: print(m, 'in base 4 is', x)
    return x

print()
base_convert(524293,4, True)
base_convert(58265,4, True)
print()





print()
print()


'''
