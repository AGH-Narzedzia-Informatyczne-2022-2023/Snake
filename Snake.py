import pygame

class Snake(object, game):
  
  def __init__(self):
    
    size = self.game.screen.get_size()
    self.length = 1
    self.speed = 1 #
    self.head_img = pygame.image.load(os.path.join("imgs","head.png")).convert_alpha()
    self.body_img = pygame.image.load(os.path.join("imgs","body.png")).convert_alpha()
    self.pos = [size[0]/2, size[1]/2]
    self.dir_h = 0
    self.dir_v = 1
    
    
  def change_dir(self):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
      self.dir_h = 0
      self.dir_v = -1
    if pressed[pygame.K_s]:
      self.dir_h = 0
      self.dir_v = 1
    if pressed[pygame.K_a]:
      self.dir_h = -1
      self.dir_v = 0
    if pressed[pygame.K_d]:
      self.dir_h = 1
      self.dir_v = 0
  
  def move(self):
    self.pos[0] +=self.dir_h*self.speed
    self.pos[1] +=self.dir_v*self.speed
  def show(self):
    
