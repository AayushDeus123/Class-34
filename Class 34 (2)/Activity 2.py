
import pygame
pygame.init()
#Create the display surface object of specific dimensions
window = pygame.display.set_mode((400,400))

#Fill the screen with white colour (using RGB)
window.fill((255,255,255))

#Define colours
green = (0,255,0)

#Draw solid circle
pygame.draw.circle(window , green , (300,300),50)

#Draw hollow circle
pygame.draw.circle(window , green , (100,100),50,3)

#Draw the surface object to the screen
pygame.display.update()

#Game loop
running = True
while running:
  #Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
#Quit Pygame
pygame.quit()