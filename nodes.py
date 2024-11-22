# This file handles the points where Pac-Man can move and turn
import pygame
import numpy as np
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
            RIGHT:None,
            PORTAL: None
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
    def __init__(self, level):
        # Create an empty list to store all our nodes
        self.level = level
        self.nodesLUT = {}
        self.nodeSymbols = ['+', 'p', 'n']
        self.pathSymbols = ['.', '-', '/', 'p']
        data = self.readMazeFile(level)
        self.createNodeTable(data)
        self.connectHorizontally(data)
        self.connectVertically(data)
        self.homekey = None

    # Reading the Text File
    def readMazeFile(self, textfile):
        return np.loadtxt(textfile, dtype='<U1')

    # Create Node Table
    def createNodeTable(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    x, y = self.constructKey(col+xoffset, row+yoffset)
                    self.nodesLUT[(x, y)] = Node(x, y)

    def constructKey(self, x, y):
        return x * TILEWIDTH, y * TILEHEIGHT

    #Connet Nodes Horizontally
    def connectHorizontally(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            key = None
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col+xoffset, row+yoffset)
                    else:
                        otherkey = self.constructKey(col+xoffset, row+yoffset)
                        self.nodesLUT[key].neighbors[RIGHT] = self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[LEFT] = self.nodesLUT[key]
                        key = otherkey
                elif data[row][col] not in self.pathSymbols:
                    key = None

        # Connet Nodes Vertically
    def connectVertically(self, data, xoffset=0, yoffset=0):
        dataT = data.transpose()
        for col in list(range(dataT.shape[0])):
            key = None
            for row in list(range(dataT.shape[1])):
                if dataT[col][row] in self.nodeSymbols:
                    if key is None:
                        key = self.constructKey(col + xoffset, row + yoffset)
                    else:
                        otherkey = self.constructKey(col + xoffset, row + yoffset)
                        self.nodesLUT[key].neighbors[DOWN] = self.nodesLUT[otherkey]
                        self.nodesLUT[otherkey].neighbors[UP] = self.nodesLUT[key]
                        key = otherkey
                elif dataT[col][row] not in self.pathSymbols:
                    key = None

    def getNodeFromPixels(self, xpixel, ypixel):
        if (xpixel, ypixel) in self.nodesLUT.keys():
            return self.nodesLUT[(xpixel, ypixel)]
        return None

    def getNodeFromTiles(self, col, row):
        x, y = self.constructKey(col, row)
        if (x, y) in self.nodesLUT.keys():
            return self.nodesLUT[(x, y)]
        return None

    # Pacman start node (temporary)
    def getStartTempNode(self):
        nodes = list(self.nodesLUT.values())
        return nodes[0]

    def createHomeNodes(self, xoffset, yoffset):
        homedata = np.array([['X', 'X', '+', 'X', 'X'],
                             ['X', 'X', '.', 'X', 'X'],
                             ['+', 'X', '.', 'X', '+'],
                             ['+', '.', '+', '.', '+'],
                             ['+', 'X', 'X', 'X', '+']])

        self.createNodeTable(homedata, xoffset, yoffset)
        self.connectHorizontally(homedata, xoffset, yoffset)
        self.connectVertically(homedata, xoffset, yoffset)
        self.homekey = self.constructKey(xoffset + 2, yoffset)
        return self.homekey

    def connectHomeNodes(self, homekey, otherkey, direction):
        key = self.constructKey(*otherkey)
        self.nodesLUT[homekey].neighbors[direction] = self.nodesLUT[key]
        self.nodesLUT[key].neighbors[direction * -1] = self.nodesLUT[homekey]

    def setPortalPair(self, pair1, pair2):
        key1 = self.constructKey(*pair1)
        key2 = self.constructKey(*pair2)
        if key1 in self.nodesLUT.keys() and key2 in self.nodesLUT.keys():
            self.nodesLUT[key1].neighbors[PORTAL] = self.nodesLUT[key2]
            self.nodesLUT[key2].neighbors[PORTAL] = self.nodesLUT[key1]

    def render(self, screen):
        # Draw all nodes and their connections
        for node in self.nodesLUT.values():
            node.render(screen)