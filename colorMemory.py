import random
import pygame

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Simon says")
clock = pygame.time.Clock()

sequenceList = []
gameRun = True

def draw():
    pygame.draw.rect(window, "green", (0, 0, 400, 400))
    pygame.draw.rect(window, "red", (400, 0, 400, 400))
    pygame.draw.rect(window, "yellow", (0, 400, 400, 400))
    pygame.draw.rect(window, "blue", (400, 400, 400, 400))

print("When inputting the sequence, seperate each value by a space")

while gameRun == True:
    sequenceList.append(random.randint(0, 3))
    print(sequenceList)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameRun = False
                exit()
        
        draw()
        pygame.display.update()
        clock.tick(60)

    responseList = input().split()
    for i in range(len(responseList)):
        responseList[i] = int(responseList[i])

    if len(responseList) == len(sequenceList):
        for i in range(len(sequenceList)):
            if responseList[i] != sequenceList [i]:
                gameRun = False
    else:
        gameRun = False