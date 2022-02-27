# coding:utf-8


def iterativeBackTrackFunc(wList, vList, C):
    def iterativeBackTrack():
        t, curX = 0, [-1]*N  # 当前深度，当前路径
        curWeight, curValue = 0, 0
        bestValue, bestX = 0, None
        while t >= 0:
            if t < N and curX[t] <= 0:
                curX[t] += 1
                if curX[t] == 0:
                    if t == N-1 and curValue > bestValue:
                        bestValue = curValue
                        bestX = curX.copy()
                    t += 1
                else:
                    if (curWeight+wList[t]) <= C:
                        curWeight += wList[t]
                        curValue += vList[t]
                        if t == N-1 and curValue > bestValue:
                            bestValue = curValue
                            bestX = curX.copy()
                        t += 1
                    else:
                        curX[t] = -1
                        t -= 1
            else:
                if t >= N:
                    t -= 1
                else:
                    curWeight -= wList[t]
                    curValue -= vList[t]
                    curX[t] = -1
                    t -= 1
        return bestValue, bestX
    
    wList = wList  # 每个物品的重量 
    vList = vList  # 每个物品的价值  
    C = C          # 背包的容量
    N = len(wList) # 物品的数量

    bestValue, bestX = iterativeBackTrack()
    print("最优值：{}， 最优解：{}".format(bestValue, bestX))


iterativeBackTrackFunc([2,8,10,8,5,7,3], [2,12,5,4,1,4,2], 20)


