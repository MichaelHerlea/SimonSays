import random
import pygame
import time

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Simon says")
clock = pygame.time.Clock()

gameSequence = []
userInputtedSequence = []

def draw():
    pygame.draw.rect(window, "green", (0, 0, 400, 400))
    pygame.draw.rect(window, "red", (400, 0, 400, 400))
    pygame.draw.rect(window, "yellow", (0, 400, 400, 400))
    pygame.draw.rect(window, "blue", (400, 400, 400, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if mousePos[0] <= 400 and mousePos[1] <= 400:
                userInputtedSequence.append(0)
            if mousePos[0] >= 400 and mousePos[1] <= 400:
                userInputtedSequence.append(1)
            if mousePos[0] <= 400 and mousePos[1] >= 400:
                userInputtedSequence.append(2)
            if mousePos[0] >= 400 and mousePos[1] >= 400:
                userInputtedSequence.append(3)

    if len(userInputtedSequence) == len(gameSequence):
        for i in range(len(gameSequence)):
            if userInputtedSequence[i] != gameSequence[i]:
                pygame.quit()
                exit()
        userInputtedSequence = []
        gameSequence.append(random.randint(0, 3))
        print(gameSequence)
        pygame.display.set_caption(f"Simon says (score: {len(gameSequence)-1})")

        for i in range(len(gameSequence)):
            if gameSequence[i] == 0:
                draw()
                pygame.draw.rect(window, "white", (0, 0, 400, 400))
                pygame.display.update()
                time.sleep(0.5)
                draw()
                pygame.display.update()
                time.sleep(0.5)
            if gameSequence[i] == 1:
                draw()
                pygame.draw.rect(window, "white", (400, 0, 400, 400))
                pygame.display.update()
                time.sleep(0.5)
                draw()
                pygame.display.update()
                time.sleep(0.5)
            if gameSequence[i] == 2:
                draw()
                pygame.draw.rect(window, "white", (0, 400, 400, 400))
                pygame.display.update()
                time.sleep(0.5)
                draw()
                pygame.display.update()
                time.sleep(0.5)
            if gameSequence[i] == 3:
                draw()
                pygame.draw.rect(window, "white", (400, 400, 400, 400))
                pygame.display.update()
                time.sleep(0.5)
                draw()
                pygame.display.update()
                time.sleep(0.5)

    draw()
    pygame.display.update()
    clock.tick(60)