import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from pellets import PelletGroup

# GameController manages the game's setup, events, updates, and rendering
class GameController(object):
    def __init__(self):
        pygame.init()                                                          # Initialize pygame (sets up everything we need to use pygame)
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)    # Create the game screen with a fixed size from constants
        self.background = None                                                  # Initialize background and clock attributes
        self.clock = pygame.time.Clock()                                        # Initialize clock attributes / Tracks time to control game speed

    # Sets up a black background surface for the game
    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()      # Create a blank surface matching the screen size
        self.background.fill(BLACK)                                         # Fill the background with the color black

    # Starts the game by setting the background and creating Pac-Man
    def startGame(self):
        self.setBackground()                            # Set up the background
        self.nodes = NodeGroup("maze1.txt")
        self.nodes.setPortalPair((0,17), (27,17))
        self.pacman = Pacman(self.nodes.getStartTempNode())    # Create a Pac-Man instance
        self.pellets = PelletGroup("maze1.txt")

    # Handles updating the game each frame
    def update(self):
        dt = self.clock.tick(30) / 1000.0   # Control the frame rate; `dt` is the time in seconds since the last frame
        self.pacman.update(dt)              # Update Pac-Man's position based on `dt`
        self.pellets.update(dt)
        self.checkPelletEvents()
        self.checkEvents()                  # Check for user inputs or quit events
        self.render()                       # Render all elements on the screen

    # Check for any events, like closing the game window
    def checkEvents(self):
        for event in pygame.event.get():    # Go through all events (e.g., key presses, closing the window)
            if event.type == QUIT:          # If the quit event is detected, exit the game
                exit()

    def checkPelletEvents(self):
        pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            self.pellets.numEaten += 1
            self.pellets.pelletList.remove(pellet)

    # Draw everything to the screen
    def render(self):
        self.screen.blit(self.background, (0,0))    # First, draw the background onto the screen
        self.nodes.render(self.screen)
        self.pellets.render(self.screen)
        self.pacman.render(self.screen)                 # Then, draw Pac-Man on top of the background
        pygame.display.update()                         # Update the display to show the new frame

# Main code to run the game
if __name__ == "__main__":
    game = GameController()             # Create the game controller and start the game
    game.startGame()
    # Keep the game running in a loop, updating every frame
    while True:
        game.update()