def grid()
    return [
    [8,5,13,23,29,15,23,30],
    [17,22,30,3,13,25,2,14],
    [10,15,18,28,2,18,27,6],
    [0,31,1,11,22,7,16,20],
    [12,17,24,26,3,24,25,5],
    [27,31,8,11,19,4,12,21],
    [21,20,28,4,9,26,7,14],
    [1,6,9,19,29,10,16,0]
    ]
end

def legalMvs(coord) # Get all legal queen moves
    x,y = coord
    temp = []
    for i in 1 .. 8
        temp << [x-i,y+i]
        temp << [x  ,y+i]
        temp << [x+i,y+i]
        temp << [x-i,y  ]
        temp << [x+i,y  ]
        temp << [x-i,y-i]
        temp << [x  ,y-i]
        temp << [x+i,y-i]
    end
    ans = []
    for c in temp
        next if c.min <= 0 or c.max >8
        ans << c
    end
    return ans
end

def getNum(coords,grid) # Find a number on a grid given coordinates
    x,y = coords
    return grid[8-y][x-1]
end

def addQ(queue, info, pos) # Ascending add into Priority Queue
    uppB, lowB = queue.length, -1
    infoPos = info[pos]
    while true
        midB = (uppB + lowB) / 2
        break if midB == lowB or infoPos == queue[midB][pos]
        lowB = midB if infoPos > queue[midB][pos]
        uppB = midB if infoPos < queue[midB][pos]
    end
    queue.insert(midB+1,info)
    return queue
end

def chkSqr(x) # Check Squares
    return false if x < 0
    return (x**0.5).to_i == x**0.5
end

def getRoute(route) # Purely for formatting Purposes to print
    str = ""
    for x,y in route
        str+= "#{(x+96).chr}#{y}, "
    end
    return str[4...str.length-2]
end

def main()
    startTime = Time.now #Start Time
    # Information in the queue presented in [Route, Score, Level]
    pQueue = [  [ [[1,1]], 0, 0 ]   ]
    max = 0
    routeHash = Hash.new(0) #Store previous points
    bestRoute = 0
    while pQueue.count > 0
        route,score,level = pQueue.pop
        g = grid().map{ |row| row.map { |a| a-level }}
        latestNode = route.last
        
        if routeHash[ [[latestNode],level] ] <= score
            routeHash[ [[latestNode],level] ]  = score # Store Scores
            startNum = getNum(latestNode,g)
            endNum = getNum([8,8],g)
            pot = legalMvs(latestNode)
            
            # Prints Best Routes
            if score + endNum > max
                if pot.index([8,8]) != nil
                    bestRoute = route + [[8,8]]
                    puts "Route: #{bestRoute.inspect}"
                    puts "Score: #{score + endNum}"
                    puts "Level: #{level}"
                    puts
                    max = score + endNum
                end
            end
            
            potNum = pot.map { |coords| [coords,getNum(coords,g)] }
            potNum.sort_by!{|a,b| b}.reverse!
            
            for coords,cNum in potNum
                numView = cNum + startNum
                break if numView < 0
                if chkSqr(numView)
                    addLvl = level + 1
                else
                    addLvl = level + 5
                end
                info = [route + [coords], score+cNum, addLvl]
                pQueue = addQ(pQueue, info, 1)
            end
        end
    end
    puts "Time Taken: #{Time.now - startTime} secs"
    return " Best Route: #{getRoute(bestRoute)} "
end 
