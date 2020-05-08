

class Node:
    def __init__(self,x):
        self.id = x
        self.grp = '---'
        self.visited = False
        self.neigh = [None]*6

class Pyramid:
    def __init__(self,N):
        self.levels = N
        self.structure = []
        self.counter = 101
        idNum = 1
        for i in range(N):
            temp = []
            for x in range(i+1):
                temp.append(Node(idNum))
                idNum += 1
            self.structure.append(temp)
        self.size = idNum-1
        for layerIdx in range(N):
            layer = self.structure[layerIdx]
            for idx in range(len(layer)):
                node = layer[idx]
                if idx != 0: node.neigh[5] = layer[idx-1]
                try : node.neigh[2] = layer[idx+1]
                except: node.neigh[2] = None
            if layerIdx == len(self.structure)-1: break
            for idx in range(len(layer)):
                layer[idx].neigh[4] = self.structure[layerIdx+1][idx]
                self.structure[layerIdx+1][idx].neigh[1] = layer[idx]
                layer[idx].neigh[3] = self.structure[layerIdx+1][idx+1]
                self.structure[layerIdx+1][idx+1].neigh[0] = layer[idx]
    
    def solve(self):
        changes = True
        while changes:
            changes = False
            for layer in self.structure:
                for d in layer:
                    if d.visited: continue                    
                    if d.neigh[4] and d.neigh[3]:
                        if not d.neigh[4].visited and not d.neigh[3].visited:
                            seq = [d.neigh[3],d.neigh[4],d]
                            for i in seq:
                                i.visited = True
                                i.grp = self.counter
                            changes = True
                            self.counter += 1
                            if not self.jam(): return False # Will never face a block this way
        
    def jam(self):
        changes = True
        while changes:
            changes = False
            for layer in self.structure:
                for d in layer:
                    if d.visited: continue
                    neighAvail = list(map(lambda x: not x.visited if x else None, d.neigh))
                    if neighAvail.count(True) == 2:
                        flag = False
                        for i in range(6):
                            if neighAvail[i] and neighAvail[i-1]: flag = True
                        if not flag: return False
                        a,b = list(filter(lambda x: not x.visited if x else False, d.neigh))
                        seq = [a,b,d]
                        for i in seq:
                            i.visited = True
                            i.grp = self.counter
                        changes = True
                        self.counter += 1
        return True

    def completed(self):
        a = {}
        for layer in self.structure:
            for d in layer:
                if not d.visited: return False
                if d.grp not in a: a[d.grp] = 1
                else: a[d.grp]+=1
        for i in a:
            if a[i] != 3: return False
        return True
        
    def print(self):
        idx = self.levels-1
        for layer in self.structure:
            strr = ' ' * int(3*idx)
            idx -= 1
            for d in layer:
                strr += str(d.grp) + '   '
            print(strr)
            

# Start
import time

ans = 0
for i in range(1,41):
    if i*(i+1)/2 %3 == 0:
        a = Pyramid(i)
        tic = time.perf_counter()
        a.solve()
        toc = time.perf_counter()
        boolC = a.completed()
        if boolC:
            print(i, f"Solved in {toc - tic:0.5f}s",boolC)
            if boolC: ans+= i
##            a.print()
print()
print("Final Answer:",ans)

'''
2 Completed: True
9 Completed: True
11 Completed: True
12 Completed: True
14 Completed: True
21 Completed: True
23 Completed: True
24 Completed: True
26 Completed: True
33 Completed: True
35 Completed: True
36 Completed: True
38 Completed: True
'''

