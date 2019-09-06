from basic import getParams

def dictFixedCount(potArr):
    counter = 0
    for key, item in potArr.items():
        if len(item) == 1: counter += 1
    return counter

def dictPrint(potArr,grid):
    grps = getParams()
    counter = 0
    for key, item in potArr.items():
#    for key, item in sorted(potArr.items(), key = lambda k:(-len(k[1]))):
        if len(item) == 1: counter += 1
        if len(item)==2:
            print("{}: {}".format(key, item))
    for grp in grps:
        for num in range(1,9):
            counterX = 0
            temp = []
            for c in grp:
                if num in potArr[c]: 
                    counterX += 1
                    temp.append(c)
            if counterX == 2:
                print(num,temp)
#        for e in grp:
#            print("{}: {}".format(e, potArr[e]))
    print("Grid Count: ",counter)
#    strr = (8,6)
#    print("X",strr,potArr[strr])
