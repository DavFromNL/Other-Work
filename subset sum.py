##subset sum problem

##Does their exist a subset of list that sums to the goal/target number.
##runs in goal*len(testBank) time


def subsetSum(goal,testBank):

    #Set up
    innerList =[]
    resultList = []
    
    for i in range(goal+1):
        resultList.append(list(innerList))
        
    resultList[0] = [0] 
    newList = list(resultList)
    
    #Start Summing
    for iii in testBank:
        print(iii)
        for iv in range(goal+1):
            
            if((resultList[iv]!= []) and (iii+iv <= goal)):
                newList[iii+iv] = list(resultList[iv])
                newList[iii+iv].append(iii)
                if(goal == sum(newList[iii+iv])):
                    print("True")
                    print(newList[iii+iv])
                    
        resultList = list(newList)
    for v in resultList:
        print(v)

while(True):
    goal = int(input("Goal: "))
    testBank = [1,4,7,10]
    subsetSum(goal,testBank)
    print()
