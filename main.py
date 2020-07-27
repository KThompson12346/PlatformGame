import pygame
import random
from settings import *
from sprites import *
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
         self.player = Player()
         self.all_sprites.add(self.player)
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

     def events(self): # Game loop - events
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
               if self.playing:
                    self.playing = False
               self.running = False

     def draw(self): # Game loop - draw
         self.screen.fill(RED)
         self.all_sprites.draw(self.screen)
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
