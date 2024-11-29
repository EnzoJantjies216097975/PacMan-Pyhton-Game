# This file stores all the fixed values used throughout the game

# Width of each tile in the game grid (measured in pixels)
TILEWIDTH = 16
# Height of each tile in the game grid (measured in pixels)
TILEHEIGHT = 16
# Number of rows in the game grid
NROWS = 36
# Number of columns in the game grid
NCOLS = 28
# Total width of the game screen, calculated based on the number of columns and tile width
SCREENWIDTH = NCOLS*TILEWIDTH
# Total height of the game screen, calculated based on the number of rows and tile height
SCREENHEIGHT = NROWS*TILEHEIGHT
# Screen size as a tuple (width, height)
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

# RGB color representation for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PINK = (255,100,150)
TEAL = (100,255,255)
ORANGE = (230,190,40)
GREEN = (0,255,0)

# Movement constants to represent directions:
STOP = 0    # Represents no movement
UP = 1      # Represents movement upward
DOWN = -1   # Represents movement downward
LEFT = 2    # Represents movement to the left
RIGHT = -2  # Represents movement to the right
PORTAL = 3  # Represents portal

# Constant to identify Pac-Man
PACMAN = 0
PELLET = 1
POWERPELLET = 2
GHOST = 3
BLINKY = 4
PINKY = 5
INKY = 6
CLYDE = 7
FRUIT = 8

SCATTER = 0
CHASE = 1
FREIGHT = 2
SPAWN = 3

SCORETXT = 0
LEVELTXT = 1
READYTXT = 2
PAUSETXT = 3
GAMEOVERTXT = 4