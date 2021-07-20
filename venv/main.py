import pygame
import random

# rozpocznij program
pygame.init()

# tworzymy ekran gry
screen = pygame.display.set_mode((800, 600))

# nazwa gry
pygame.display.set_caption("Kunai")

# ikona gry
icon = pygame.image.load("assets/kunai.png")
pygame.display.set_icon(icon)

# gracz
zawodnik = pygame.image.load("assets/celtic.png")
playerX = 368
playerY = 536
speedX = 0
speedY = 0

# przeciwnik
przeciwnik = pygame.image.load("assets/sado.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(20, 250)
enemySpeedX = 0.3

# ikona strzalu
strzala = pygame.image.load("assets/kunai.png")
arrowX = 0
arrowY = 0
arrowSpeedY = 0.2
arrowState = "ready"


def player(x, y):
    screen.blit(zawodnik, (x, y))


def enemy(x, y):
    screen.blit(przeciwnik, (x, y))


def arrow(x, y):
    global arrowState
    arrowState = "throw"
    screen.blit(strzala, (x + 0.2 , y +0.2))


running = True

while running:
    screen.fill((255, 195, 160))  # R G B (red, green, blue) 0->255

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                arrowY = playerY
                arrow(playerX, arrowY)


    #ruch klawiatury
    keys = pygame.key.get_pressed()
    speedX = 0
    speedY = 0
    if keys[pygame.K_LEFT]:
        speedX = -0.2
    elif keys[pygame.K_RIGHT]:
        speedX = 0.2

    if keys[pygame.K_UP]:
        speedY = -0.2
    elif keys[pygame.K_DOWN]:
        speedY = 0.2

    playerX += speedX
    playerY += speedY

    # ograniczanie obszaru mapy
    if playerX <= 1:
        playerX = 1
    elif playerX >= 735:
        playerX = 735

    if playerY <= 1:
        playerY = 1
    elif playerY >= 536:
        playerY = 536

    # ograniczanie obszaru mapy przeciwnika
    if enemyX <= 1:
        enemySpeedX *= -1
        enemyY += 32
    elif enemyX >= 735:
        enemySpeedX *= -1
        enemyY += 32

    enemyX += enemySpeedX

    player(playerX, playerY)

    #strzal
    if arrowState is "throw":
        arrow(playerX, arrowY)
        arrowY -= arrowSpeedY

    enemy(enemyX, enemyY)

    pygame.display.update()
