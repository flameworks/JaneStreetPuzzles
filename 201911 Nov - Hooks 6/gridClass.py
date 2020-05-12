class grid:
    def __init__(self, h):
        self.g = [[0] * h for i in range(h)]
        self.h = h
        
    def printer(self,spacing=2):
        headerStr = "   "
        for i in range(self.h):
            headerStr += str(i)
            headerStr += " " * (spacing-len(str(i))+1)
        print(headerStr)
        for cnt in range(self.h):
            row = self.g[cnt]
            strr = str(cnt) + "|"
            if cnt < 10: strr = " " + str(cnt) + "|"
            for i in range(self.h):
                strr += " " * (spacing-len(str(row[i])))
                if row[i] < 0: strr += ". "
                if row[i] == 0: strr += " "
                if row[i] > 0: strr += str(row[i])
                if i < self.h-1: strr += "|"
            strr += "|" + str(cnt)
            print(strr)
        print(headerStr)
        
        
        
