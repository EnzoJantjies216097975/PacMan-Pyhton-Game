import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from pellets import PelletGroup
from ghosts import GhostGroup
from fruit import Fruit
from pauser import Pause

# GameController manages the game's setup, events, updates, and rendering
class GameController(object):
    def __init__(self):
        pygame.init()                                                          # Initialize pygame (sets up everything we need to use pygame)
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)    # Create the game screen with a fixed size from constants
        self.background = None                                                  # Initialize background and clock attributes
        self.clock = pygame.time.Clock()                                        # Initialize clock attributes / Tracks time to control game speed
        self.fruit = None
        self.pause = Pause(True)
        self.level = 0
        self.lives = 5

    def restartGame(self):
        self.lives = 5
        self.level = 0
        self.pause.paused = True
        self.fruit = None
        self.startGame()

    def resetLevel(self):
        self.pause.paused = True
        self.pacman.reset()
        self.ghosts.reset()
        self.fruit = None

    def nextLevel(self):
        self.showEntities()
        self.level += 1
        self.pause.paused = True
        self.startGame()

    # Sets up a black background surface for the game
    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()      # Create a blank surface matching the screen size
        self.background.fill(BLACK)                                         # Fill the background with the color black

    # Starts the game by setting the background and creating Pac-Man
    def startGame(self):
        self.setBackground()
        self.nodes = NodeGroup("maze1.txt")
        self.nodes.setPortalPair((0,17), (27,17))
        homekey = self.nodes.createHomeNodes(11.5, 14)
        self.nodes.connectHomeNodes(homekey, (12,14), LEFT)
        self.nodes.connectHomeNodes(homekey, (15,14), RIGHT)
        self.pacman = Pacman(self.nodes.getNodeFromTiles(15, 26))
        self.pellets = PelletGroup("maze1.txt")
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)
        self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 0+14))
        self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))
        self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(0+11.5, 3+14))
        self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(4+11.5, 3+14))
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(2+11.5, 3+14))

    # Handles updating the game each frame
    def update(self):
        dt = self.clock.tick(30) / 1000.0   # Control the frame rate; `dt` is the time in seconds since the last frame
        self.pellets.update(dt)
        if not self.pause.paused:
            self.pacman.update(dt)  # Update Pac-Man's position based on `dt`
            self.ghosts.update(dt)
            if self.fruit is not None:
                self.fruit.update(dt)
            self.checkPelletEvents()
            self.checkGhostEvents()
            self.checkFruitEvents()
        afterPausedMethod = self.pause.update(dt)
        if afterPausedMethod is not None:
            afterPausedMethod()
        self.checkEvents()                  # Check for user inputs or quit events
        self.render()                       # Render all elements on the screen

    def checkGhostEvents(self):
        for ghost in self.ghosts:
        if self.pacman.collideGhost(ghost):
            if ghost.mode.current is FREIGHT:
                self.pacman.visible = False
                ghost.visible = False
                self.pause.setPause(pauseTime=1, func=self.showEntities)
                ghost.startSpawn()
            elif ghost.mode.current is not SPAWN:
                if self.pacman.alive:
                    self.lives -= 1
                    self.pacman.die()
                    self.ghosts.hide()
                    if self.lives <= 0:
                        self.pause.setPause(pauseTime=3, func=self.restartGame)
                    else:
                        self.pause.setPause(pauseTime=3, func=self.resetLevel)

    def showEntities(self):
        self.pacman.visible = True
        self.ghosts.show()

    def hideEntities(self):
        self.pacman.visible = False
        self.ghosts.hide()

    # Check for any events, like closing the game window
    def checkEvents(self):
        for event in pygame.event.get():    # Go through all events (e.g., key presses, closing the window)
            if event.type == QUIT:          # If the quit event is detected, exit the game
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if self.pacman.alive:
                        self.pause.setPause(playerPaused=True)
                        if not self.pause.paused:
                            self.showEntities()
                        else:
                            self.hideEntities()

    def checkPelletEvents(self):
        pellet = self.pacman.eatPellets(self.pellets.pelletList)
        if pellet:
            self.pellets.numEaten += 1
            self.pellets.pelletList.remove(pellet)
            if pellet.name == POWERPELLET:
                self.ghosts.startFreight()
            if self.pellets.isEmpty():
                self.hideEntities()
                self.pause.setPause(pauseTime=3, func=self.nextLevel)

    def checkFruitEvents(self):
        if self.pellets.numEaten == 50 or self.pellets.numEaten == 140:
            if self.fruit is None:
                self.fruit = Fruit(self.nodes.getNodeFromTiles(9, 20))
        if self.fruit is not None:
            if self.pacman.collideCheck(self.fruit):
                self.fruit = None
            elif self.fruit.destroy:
                self.fruit = None

    # Draw everything to the screen
    def render(self):
        self.screen.blit(self.background, (0,0))    # First, draw the background onto the screen
        self.nodes.render(self.screen)
        self.pellets.render(self.screen)
        if self.fruit is not None:
            self.fruit.render(self.screen)
        self.pacman.render(self.screen)                 # Then, draw Pac-Man on top of the background
        self.ghosts.render(self.screen)
        pygame.display.update()                         # Update the display to show the new frame

# Main code to run the game
if __name__ == "__main__":
    game = GameController()             # Create the game controller and start the game
    game.startGame()
    # Keep the game running in a loop, updating every frame
    while True:
        game.update()