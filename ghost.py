import pygame
import random
import time
from settings import WIDTH, CHAR_SIZE, GHOST_SPEED

class Ghost(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        super().__init__()
        self.abs_x = (row * CHAR_SIZE)
        self.abs_y = (col * CHAR_SIZE)
        self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
        self.move_speed = GHOST_SPEED
        self.color = pygame.Color(color)
        self.move_directions = [(-1,0),(0,-1),(1,0),(0,1)]
        self.moving_dir = "up"
        self.img_path = f'assets/ghosts/{color}/'
        self.img_name = f'{self.moving_dir}.png'
        self.image = pygame.image.load(self.img_path + self.img_name)
        self.image = pygame.transform.scale(self.image, (CHAR_SIZE, CHAR_SIZE))
        self.rect = self.image.get_rect(topleft = (self.abs_x, self.abs_y))
        self.mask = pygame.mask.from_surface(self.image)
        self.directions = {'left': (-self.move_speed, 0), 'right': (self.move_speed, 0), 'up': (0, -self.move_speed), 'down': (0, self.move_speed)}
        self.keys = ['left', 'right', 'up', 'down']
        self.direction = (0, 0)

    def move_to_start_pos(self):
        self.rect.x = self.abs_x
        self.rect.y = self.abs_y

    def is_collide(self, x, y, walls_collide_list):
        tmp_rect = self.rect.move(x, y)
        if tmp_rect.collidelist(walls_collide_list) == -1:
            return False
        return True
    
    def _animate(self):
        self.img_name = f'{self.moving_dir}.png'
        self.image = pygame.image.load(self.img_path + self.img_name)
        self.image = pygame.transform.scale(self.image, (CHAR_SIZE, CHAR_SIZE))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

    def update(self, walls_collide_list):
        # ghost movement
        available_moves = []
        for key in self.keys:
            if not self.is_collide(*self.directions[key], walls_collide_list):
                available_moves.append(key)
        randomizing = False if len(available_moves) <= 2 and self.direction != (0,0) else True
        # 60% chance of randomizing ghost move
        if randomizing and random.randrange( 0,100 ) <= 60:
            self.moving_dir = random.choice(available_moves)
            self.direction = self.directions[self.moving_dir]
        if not self.is_collide(*self.direction, walls_collide_list):
            self.rect.move_ip(self.direction)
        else:
            self.direction = (0,0)
        # teleporting to the other side of the map
        if self.rect.right <= 0:
            self.rect.x = WIDTH
        elif self.rect.left >= WIDTH:
            self.rect.x = 0
        self._animate()

# The constructor (__init__) initializes the ghost with its starting position (row, col) and color (color). 
# abs_x and abs_y store the absolute pixel position of the ghost based on its row and column multiplied by CHAR_SIZE. 
# The rect defines the rectangular area occupied by the ghost on the screen using pygame. Rect. 
# The move_directions is a list of tuples representing possible movement directions (left, up, right, down). 
# The moving_dir initializes the ghost's movement direction as "up". 
# The img_path and img_name specify the path to the ghost's image file (img_name is based on moving_dir). 
# The image loads the ghost's image and scales it to CHAR_SIZE using pygame.image.load() and pygame.transform.scale(). 
# The mask creates a collision mask for the ghost's image using pygame.mask.from_surface().
# The move_to_start_pos() set the ghost's position back to its initial coordinates (abs_x, abs_y). 
# The is_collide(x, y, walls_collide_list) checks if the ghost collides with any walls based on a temporary movement (x, y).
# The _animate() updates the ghost's image (image) based on its current movement direction (moving_dir). 
# The update(walls_collide_list) updates the ghost's position and behavior based on collision with walls (walls_collide_list). 
# It checks available movement directions (available_moves) by iterating through self.keys (['left', 'right', 'up', 'down']) and determining if they do not cause a collision. 
# It randomizes the self.moving_dir if available moves are limited or randomly chosen. Then moves the ghost (self.rect.move_ip(self. direction)) if the movement direction is valid. 
# It handles teleportation to the opposite side of the screen if the ghost reaches the screen boundary.