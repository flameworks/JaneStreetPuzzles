def removeEasy(x):
    while 'SRSRSR' in x or 'RR' in x:        
        x = x.replace('RR','')
        x = x.replace('SRSRSR','') 
    return x

def solve(command):
    answer = ''
    flag = True
    for c in command:
        if c == ' ': continue
        if answer:
            if c == answer[0]: answer = answer[1:]
            else:
                if c == 'S': answer = 'RSRSR' + answer
                elif c == 'R': answer = 'R' + answer
        else:
            if c == 'R': flag = not flag # Bool switch accepting any S
            elif c == 'S' and flag: answer = 'RS'
        answer = removeEasy(answer)   
    return answer


import time
tic = time.perf_counter()
command = 'SRSRRSSRSRSSRSSRRSSRSSSSSRSSRSSRSRSSRSSRSSSSSSSSRSSRSSSSSRSSRSSRRSSRSSSSSRSSRSSRSSSSSSSSSSSSSSSSSRSSRSSRS'
ans1 = solve(command)
print('Command length',len(command))
print('Simplified command length',len(removeEasy(command)))
print()
print(f'Result (length {len(ans1)}): {ans1}')
toc = time.perf_counter()
print()
print(f'Completed in {toc - tic:0.5f}s')
