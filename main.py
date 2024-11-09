import pygame
import random
from enum import Enum
from typing import List, Tuple, Dict

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    STOP = (0, 0)

class GameState(Enum):
    PLAYING = 1
    PAUSED = 2
    GAME_OVER = 3
    LEVEL_COMPLETE = 4

class Entity:
    def __init__(self, x: int, y: int, speed: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = Direction.STOP
        self.next_direction = Direction.STOP
        self.animation_frame = 0
        
    def move(self, walls: List['Wall']):
        next_x = self.x + self.direction.value[0] * self.speed
        next_y = self.y + self.direction.value[1] * self.speed
        
        if not self.check_collision(next_x, next_y, walls):
            self.x = next_x
            self.y = next_y
            
    def check_collision(self, x: float, y: float, walls: List['Wall']) -> bool:
        for wall in walls:
            if wall.contains_point(x, y):
                return True
        return False
