# will hold the sprite classes
import pygame
from settings import *
import random
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.on_ground = True

    def jump(self):
        # jump only if on a platform
        if self.on_ground:
            self.vel.y = -20
            self.on_ground = False

    def events(self, event):
        if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   self.jump()

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        # equations of motion
        self.vel += self.acc
        #self.pos += self.vel + 0.5 * self.acc

        # Side collisions
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.rect.centerx = self.pos.x

        # Stop from going of the left side of screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.centerx

        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)

        if hits:
            if self.vel.x > 0: # moving right
                self.rect.right = hits[0].rect.left
                self.pos.x = self.rect.centerx
                self.vel.x = 0
            elif self.vel.x < 0: # moving left
                self.rect.left = hits[0].rect.right
                self.pos.x = self.rect.centerx
                self.vel.x = 0

        # top and bottom collisions
        self.pos.y += self.vel.y + 0.5 * self.acc.y
        self.rect.centery = self.pos.y
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if hits:
            if self.vel.y > 0: # collision with the top of a platform
                self.rect.bottom = hits[0].rect.top
                self.pos.y = self.rect.centery
                self.vel.y = 0
                self.on_ground = True
            elif self.vel.y < 0: # collision with the bottom of a platform
                self.rect.top = hits[0].rect.bottom
                self.pos.y = self.rect.centery
                self.vel.y = 0


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
