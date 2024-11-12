import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman

# GameController manages the game's setup, events, updates, and rendering
class GameController(object):
    def __init__(self):
        # Initialize pygame (sets up everything we need to use pygame)
        pygame.init()
        # Create the game screen with a fixed size from constants
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        # Initialize background and clock attributes
        self.background = None
        self.clock = pygame.time.Clock()    # Tracks time to control game speed

    # Sets up a black background surface for the game
    def setBackground(self):
        # Create a blank surface matching the screen size
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        # Fill the background with the color black
        self.background.fill(BLACK)

    # Starts the game by setting the background and creating Pac-Man
    def startGame(self):
        self.setBackground()            # Set up the background
        self.pacman = Pacman()          # Create a Pac-Man instance

    # Handles updating the game each frame
    def update(self):
        # Control the frame rate; `dt` is the time in seconds since the last frame
        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)          # Update Pac-Man's position based on `dt`
        self.checkEvents()              # Check for user inputs or quit events
        self.render()                   # Render all elements on the screen

    # Check for any events, like closing the game window
    def checkEvents(self):
        # Go through all events (e.g., key presses, closing the window)
        for event in pygame.event.get():
            if event.type == QUIT:      # If the quit event is detected, exit the game
                exit()

    # Draw everything to the screen
    def render(self):
        self.screen.blit(self.background, (0,0))    # First, draw the background onto the screen
        self.pacman.render(self.screen)                 # Then, draw Pac-Man on top of the background
        pygame.display.update()                         # Update the display to show the new frame

# Main code to run the game
if __name__ == "__main__":
    game = GameController()             # Create the game controller and start the game
    game.startGame()
    # Keep the game running in a loop, updating every frame
    while True:
        game.update()