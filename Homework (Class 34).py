import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
WHITE = (255, 255, 255)

font = pygame.font(None, 36)
text = font.render("Hello Pygame!", True, WHITE)

rect = pygame.Rect(220, 190, 200, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, rect)
    screen.blit(text, (240, 220))
    pygame.display.flip()

pygame.quit()