import pygame
from settings import *
# A camera that keeps track of an offset that will be, how far we want to draw the screen which will include all objects on the screen. We are just shifting the drawing of our screen according to the offset. Camera needs to do two things, apply the offset and then update the movement of where the player is on the screen.
class Camera:
    def __init__(self, width, height): # we will need to tell the camera how wide and high we want it to be
        self.camera = pygame.Rect(0, 0, width, height) # is the rectangle we set to keep track of the screen/be the camera
        self.width = width
        self.height = height

    def apply(self, entity): # method to apply the offset to the screen, by shifting the screen according to the movement of the entity within the camera screen
        return entity.rect.move(self.camera.topleft)

    def update(self, target): # method to update where the player/target has moved to, updates are done according to last known position of the target
        # as the target moves the camera moves in the opposite direction of the target and stays within the center of the screen
        x = -target.rect.x + int(WIDTH/2)  # left to right
        y = -target.rect.y + int(HEIGHT/2) # up and down

        # limit scrolling to map size, keeps the 'camera' from going over the edges
        x = min(0, x) # left
        y = min(0, y) # top
        y = max(-(self.height - HEIGHT), y) # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height) # adjusts the camera's rectangle with the new x and y 
