import pygame
pygame.init()
dis=pygame.display.set_mode((1440,720))
pygame.display.update()
pygame.display.set_caption('GigaSnake')
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
 
pygame.quit()
quit()
