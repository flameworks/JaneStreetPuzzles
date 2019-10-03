def printer(y):
    topLine = "   "
    for i in range(17):
        topLine += "  " + str(i)
        if i < 9: topLine += " "
    print(topLine)
    for cnt in range(17):
        row = y[cnt]
        strr = str(cnt) + "|"
        if cnt < 10: strr = " " + str(cnt) + "|"
        for i in range(17):
            if row[i] == 99:
                strr += " @ "
            elif row[i] == -99:
                strr += " .."
            elif row[i] < -9: 
                strr += "x" + str(abs(row[i]))
            elif row[i] < 0:
                strr += " x" + str(abs(row[i]))
            elif row[i] == 0:
                strr += "   "
            elif row[i] < 10:
                strr += "  " + str(row[i])
            else:
                strr += " " + str(row[i])
            strr += "|"
        strr += str(cnt)
        print(strr)
    print(topLine)

def getGrid():
    g = [None] * 17
    for i in range(17):
        g[i] = [0] * 17
    g[10][0] = 4;     g[13][0] = 6;     g[2][0] = 4;      g[6][11] = 3;     g[6][1] = 7
    g[15][2] = 12;    g[5][2] = 3;      g[16][3] = 2;     g[1][3] = 12;     g[12][3] = 9
    g[14][16] = 6;    g[14][11] = 7;    g[15][13] = 4;    g[14][4] = 3;     g[16][7] = 18;
    g[0][9] = 8;      g[4][7] = 7;      g[0][13] = 2;     g[1][14] = 7;     g[3][16] = 5
    g[4][13] = 10;    g[8][8] = 20;     g[11][14] = 8;    g[12][9] = 11;    g[10][15] = 18
    g[2][12] = 3;     g[6][16] = 3;     g[10][5] = 14;    g[2][5] = 10
    return g
