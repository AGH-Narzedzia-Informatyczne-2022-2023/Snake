import pygame
import constants

pygame.init()

screen = pygame.display.set_mode([constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

pygame.quit()
