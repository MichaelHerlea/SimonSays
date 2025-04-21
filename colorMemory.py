import random

sequenceList = []
gameRun = True

while gameRun == True:
    sequenceList.append(random.randint(0, 3))
    print(sequenceList)

    responseList = input("Input the sequence (seperate each value by a space): ").split()
    for i in range(len(responseList)):
        responseList[i] = int(responseList[i])

    if len(responseList) == len(sequenceList):
        for i in range(len(sequenceList)):
            if responseList[i] != sequenceList [i]:
                gameRun = False
    else:
        gameRun = False