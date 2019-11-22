import time
def main(mountainArr):
    mountainArr.append(mountainArr[-1])
    workingList = []
    maxHeight = -1
    mountainArrLen = len(mountainArr)-1
    for mDx in range(mountainArrLen):
        h = mountainArr[mDx];   h1 = mountainArr[mDx+1]
        workLen = len(workingList)
#        print(h,workingList, maxHeight)
        for idx in range(workLen):
            localM, localMinPt = workingList.pop(0)
            if h >= localM:
                if localM - localMinPt > maxHeight: maxHeight = localM - localMinPt
                continue
            workingList.append([localM,min(h,localMinPt)])
        if h > h1: workingList.append([h,h1])
    return maxHeight
    
# Create Array
start = time.time()
m = [2,2,5,2,8,3,5,7,3,3,4,5,7,9,5,2,3,6,7,8,9,6,4,1,5,3,5,7]
m *= 10000
end = time.time()
print("Time Taken: ",end - start)     
print()  
print("Solution:")  

# Analysis time
start = time.time()
x = main(m)
print(x)
end = time.time()
print("Time Taken: ",end - start)       



#import time
#def main(mountainArr):
#    workingList = []
#    maxHeight = -1
#    for h in mountainArr:
#        workLen = len(workingList)
#        print(h,workingList, maxHeight)
#        for idx in range(workLen):
#            localM, localMinPt = workingList.pop(0)
#            if h < localM: 
#                if localMinPt == -1: localMinPt = h
#                else: localMinPt = min(h,localMinPt)
#                newH = h - localMinPt
#                if newH > maxHeight: maxHeight = newH
#                workingList.append([localM,localMinPt])                
#            else:
#                if localMinPt != -1 and localM - localMinPt > maxHeight: 
#                    maxHeight = localM - localMinPt
#        workingList.append([h,-1])
#    return maxHeight
