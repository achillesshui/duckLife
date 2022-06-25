import pygame
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FIRST GAME: DUCKLIFE SWIM")

mainC = pygame.Rect(WIDTH/2 - 100, HEIGHT/2, 50, 50)
playerScore = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE_FONT = pygame.font.SysFont("comicsans", 50)

FPS = 60
LRVEL = 5
UDVEL = 100
GRAVITY = 2

JUMP = pygame.USEREVENT + 1

def drawWindow():
    WIN.fill(WHITE)    
    scoreText = SCORE_FONT.render("SCORE: " + str(playerScore), 1, BLACK)
    WIN.blit(scoreText, (10, 10))
    pygame.draw.rect(WIN, BLACK, mainC)
    pygame.display.update()


def playerLRMovement(keysPressed):
    if keysPressed[pygame.K_LEFT]:
        mainC.x -= LRVEL
    if keysPressed[pygame.K_RIGHT]:
        mainC.x += LRVEL

def playerUDMovement():
    mainC.y -= LRVEL

def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        if mainC.y >= HEIGHT/2:
            mainC.y -= GRAVITY
        if mainC.y <= HEIGHT/2:
            mainC.y += GRAVITY


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and mainC.y >= 0:
                    mainC.y -= GRAVITY

                if event.key == pygame.K_DOWN and mainC.y <= HEIGHT:
                    mainC.y += UDVEL
                    break

        keysPressed = pygame.key.get_pressed()
        playerLRMovement(keysPressed)
        # playerUDMovement()

        drawWindow()
    
    main()
    

if __name__ == "__main__":
    main()
    