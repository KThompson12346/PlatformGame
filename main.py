import pygame
import random
from settings import *
from sprites import *
from camera import *
from os import path
class Game:
     def __init__(self):
          pygame.init() # initialises pygame
          pygame.mixer.init()
          self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # sets the width and height of the pygame window
          pygame.display.set_caption(TITLE)
          self.clock = pygame.time.Clock()
          self.running = True
          self.font_name = pygame.font.match_font(FONT_NAME)
          self.load_data()

     def load_data(self):
         pass

     def new(self):
         self.all_sprites = pygame.sprite.Group()
         self.platforms = pygame.sprite.Group()
         self.player = Player(self)
         self.all_sprites.add(self.player)
         for plat in PLATFORM_LIST:
             p = Platform(*plat)
             self.all_sprites.add(p)
             self.platforms.add(p)
         self.camera = Camera(WIDTH, HEIGHT) # creates the camera with WIDTH and HEIGHT of the screen
         self.run()

     def run(self): # Game Loop - runs the game
         self.playing = True
         while self.playing:
             self.clock.tick(FPS)
             self.events()
             self.update()
             self.draw()

     def update(self): # Game loop - update
         self.all_sprites.update()
         # collision with top of platform
         if self.player.vel.y > 0:
              hits = pygame.sprite.spritecollide(self.player, self.platforms, False) # returns a list of platform sprites that hit the player
              if hits:
                   self.player.pos.y = hits[0].rect.top
                   self.player.vel.y = 0
         # collision with the bottom of a platform
         if self.player.vel.y < 0:
              hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
              if hits:
                   self.player.top = hits[0].rect.bottom
                   self.player.vel.y = -self.player.vel.y

         # screen moves with player
         self.camera.update(self.player) # is the camera that tracks players movement

     def events(self): # Game loop - events
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  if self.playing:
                      self.playing = False
                  self.running = False
             if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                    self.player.jump()

     def draw(self): # Game loop - draw
         self.screen.fill(RED)
         #self.all_sprites.draw(self.screen)
         for sprite in self.all_sprites:
              self.screen.blit(sprite.image, self.camera.apply(sprite)) # loops through the all_sprites group and blit's each sprite onto the screen
         pygame.display.flip()

     def start_screen(self):
         pass

     def game_over_screen(self):
         pass

     def wait_for_key(self):
         pass

     def draw_text(self,text, size, colour, x, y):
         pass

g = Game()
g.start_screen()
while g.running:
     g.new()
     g.game_over_screen()

pygame.quit()
