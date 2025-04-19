import random

sequenceList = []
gameFail = False

while gameFail == False:
    sequenceList.append(random.randint(0, 3))
    print(sequenceList)

    responseList = input("Input the sequence (seperate each value by a space): ").split()
    for i in range(len(responseList)):
        responseList[i] = int(responseList[i])

    if len(responseList) == len(sequenceList):
        for i in range(len(sequenceList)):
            if responseList[i] != sequenceList [i]:
                gameFail = True
    else:
        gameFail = True