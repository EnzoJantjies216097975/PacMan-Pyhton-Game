# This file handles the points where Pac-Man can move and turn
import pygame
from vector import Vector2
from constants import *

"""
A Node is like an intersection in the game maze.
It's a point where Pac-Man can:
- Change direction
- Make decisions about where to go next
"""
class Node(object):
    def __init__(self, x, y):
        # Create a new node at position (x,y)
        self.position = Vector2(x, y)
        # Keep track of which other nodes this one connects to
        # We store None if there's no connection in that direction
        self.neighbors = {
            UP:None,
            DOWN:None,
            LEFT:None,
            RIGHT:None
        }

    def render(self, screen):
        # Draw this node and its connections on the screen
        # Loop through each possible direction
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                # Draw a white line from this node to its neighbor
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                # Draw a red circle at this node's position
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)


"""
NodeGroup manages all the nodes in the game.
It's like a map that keeps track of all intersections
and how they connect to each other.
"""
class NodeGroup(object):
    def __init__(self):
        # Create an empty list to store all our nodes
        self.nodeList = []

    # Store all nodes in our list so we can work with them later
    def setupTestNodes(self):
        # Create a test maze layout with connected nodes
        # First, create all the nodes
        nodeA = Node(80, 80)
        nodeB = Node(160, 80)
        nodeC = Node(80, 160)
        nodeD = Node(160, 160)
        nodeE = Node(208, 160)
        nodeF = Node(80, 320)
        nodeG = Node(208, 320)

        # Then connect the nodes to create paths
        # Each connection is made both ways (if A connects to B, B connects to A)

        nodeA.neighbors[RIGHT] = nodeB
        nodeA.neighbors[DOWN] = nodeC
        nodeB.neighbors[LEFT] = nodeA
        nodeB.neighbors[DOWN] = nodeD
        nodeC.neighbors[UP] = nodeA
        nodeC.neighbors[RIGHT] = nodeD
        nodeC.neighbors[DOWN] = nodeF
        nodeD.neighbors[UP] = nodeB
        nodeD.neighbors[LEFT] = nodeC
        nodeD.neighbors[RIGHT] = nodeE
        nodeE.neighbors[LEFT] = nodeD
        nodeE.neighbors[DOWN] = nodeG
        nodeF.neighbors[UP] = nodeC
        nodeF.neighbors[RIGHT] = nodeG
        nodeG.neighbors[UP] = nodeE
        nodeG.neighbors[LEFT] = nodeF
        self.nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

    def render(self, screen):
        # Draw all nodes and their connections
        for node in self.nodeList:
            node.render(screen)