# Game options/settings
TITLE = 'Platformer'
WIDTH = 900
HEIGHT = 500
FPS = 60
FONT_NAME = 'arial'
HS_FILE = 'highscore.txt'
SPRITESHEET = 'spritesheet_jumper.png'

# Game colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Starting Platforms:
PLATFORM_LIST = [(0, HEIGHT - 50,  WIDTH, 50), (WIDTH / 2, HEIGHT * 1 / 2, 200, 30), (WIDTH + 150, HEIGHT - 50, WIDTH, 50)]
# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
