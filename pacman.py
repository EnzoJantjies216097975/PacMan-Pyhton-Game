import pygame
from pygame.locals import *
from vector import Vector2
from constants import *


# Define the Pacman class, which will control Pac-Man's properties and behavior
class Pacman(object):
    def __init__(self, node):
        self.name = PACMAN                          # Set Pac-Man's name (identifier)
        # self.position = Vector2(200, 400)       # Set Pac-Man's initial position on the screen
        self.directions = {                         # Define possible directions Pac-Man can move in using vectors
            STOP:Vector2(),                         # No movement
            UP:Vector2(0,-1),                       # Move up
            DOWN:Vector2(0,1),                  # Move down
            LEFT:Vector2(-1,0),                     # Move left
            RIGHT:Vector2(1,0)}                 # Move right
        self.direction = STOP
        self.speed = 100 * TILEWIDTH/16
        # Set Pac-Man's speed, adjusting based on tile width
        self.radius = 10                            # Radius for Pac-Man's circular shape
        self.color = YELLOW                         # Color of Pac-Man
        self.node = node
        self.setPosition()
        self.target = node

    def setPosition(self):
        self.position = self.node.position.copy()

    # Update Pac-Man's position based on time passed and current direction
    def update(self, dt):
        self.position += self.directions[self.direction]*self.speed*dt     # Adjust position by moving in the current direction with speed and time (dt)
        # Get any valid key (if pressed) to update the direction
        direction = self.getValidKey()
        # self.direction = direction
        # self.node = self.getNewTarget(direction)
        # self.setPosition()
        if self.overshotTarget():
            self.node = self.target
            self.target = self.getNewTarget(direction)
            if self.target is not self.node:
                self.direction = direction
            #else:
            #    self.direction = STOP
            #    self.setPosition()
            else:
                self.target = self.getNewTarget(self.direction)

            if self.target is self.node:
                self.direction = STOP
            self.setPosition()
        else:
            if self.oppositeDirection(direction):
                self.reverseDirection()

    def validDirection(self, direction):
        if direction is not STOP:
            if self.node.neighbors[direction] is not None:
                return True
        return False

    def getNewTarget(self, direction):
        if self.validDirection(direction):
            return self.node.neighbors[direction]
        return self.node

    # Check if a valid movement key is pressed, and return that direction
    def getValidKey(self):
        key_pressed = pygame.key.get_pressed()                  # Check for keys being pressed
        if key_pressed[K_UP]:
            return UP
        if key_pressed[K_DOWN]:
            return DOWN
        if key_pressed[K_LEFT]:
            return LEFT
        if key_pressed[K_RIGHT]:
            return RIGHT
        return STOP                                             # No key is pressed, so stop movement

    def overshotTarget(self):
        if self.target is not None:
            vec1 = self.target.position - self.node.position
            vec2 = self.position - self.node.position
            node2Target = vec1.magnitudeSquared()
            node2Self = vec2.magnitudeSquared()
            return node2Self >= node2Target
        return False

    def reverseDirection(self):
        self.direction *= -1
        temp = self.node
        self.node = self.target
        self.target = temp

    def oppositeDirection(self, direction):
        if direction is not STOP:
            if direction == self.direction * -1:
                return True
        return False

    # Render (draw) Pac-Man on the screen
    def render(self, screen):
        p = self.position.asInt()                               # Convert position to integer coordinates for drawing
        pygame.draw.circle(screen, self.color, p, self.radius)  # Draw Pac-Man as a circle at the current position on the screen