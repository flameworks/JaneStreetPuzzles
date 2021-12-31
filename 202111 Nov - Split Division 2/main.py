
from longD import *
from methods import *

import time
tic = time.perf_counter()

ans = []


##gridArr = ['xx1x','xx2','xxx5647','33xxx','1xx34','1xx8','xxx7','xxxx','3x']
gridArr = ['3x22','4x2','x7xxx23','xxxx2','xxxx2','9x38','x3x23','x3272','37']

for divisor in range(1000,10000):
    if not verify(divisor, gridArr[0] ): continue

    for quotient in range(100,1000):
        if not verify(quotient,gridArr[1]): continue
                
        for remainder in range(10,100):
            if not verify(remainder,gridArr[8]): continue
            
            dividend = quotient*divisor+remainder
            if not verify(dividend,gridArr[2]): continue
            
            lineA = division(dividend ,divisor).lineA
            if len(lineA) != 6: continue

            if not verify(lineA[0],gridArr[3]): continue
            if not verify(lineA[1],gridArr[4]): continue
            if not verify(lineA[2],gridArr[5]): continue
            if not verify(lineA[3],gridArr[6]): continue
            if not verify(lineA[4],gridArr[7]): continue
            
            ans.append( (dividend,divisor) )

toc = time.perf_counter()
print(f'{len(ans)} answers found in {toc - tic:0.5f}s')
for x in ans:
    print(x)
print()

print('Filtering answers')
for idx, i in enumerate(ans):
    x1,y1 = i
    for j in ans[idx+1:]:
        x2,y2 = j
        if i == j: continue
        if division(x1,y1).compare( division(x2,y2), gridArr):
            print(f'The answer is {x1+x2:,}')
            print()
            division(x1,y1).pprint()
            print()
            division(x2,y2).pprint()
            print()

############# TIMER
toc = time.perf_counter()
print(f'All completed in {toc - tic:0.5f}s')

