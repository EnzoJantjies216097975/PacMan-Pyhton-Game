import pygame
import random
import time
from settings import WIDTH, CHAR_SIZE, GHOST_SPEED

# Define the Ghost class, inheriting from pygame's Sprite class
class Ghost(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        super().__init__()                                                                                                                                  # Call the parent class (Sprite) constructor
       
        # Set initial position based on row and column, scaled by character size
        self.abs_x = row * CHAR_SIZE
        self.abs_y = col * CHAR_SIZE

        # Create a rectangular representation of the ghost at the starting position
        self.rect = pygame.Rect(self.abs_x, self.abs_y, CHAR_SIZE, CHAR_SIZE)
        
         # Set the ghost's movement speed and color
        self.move_speed = GHOST_SPEED
        self.color = pygame.Color(color)
        
         # List of possible movement directions (left, up, right, down)
        self.move_directions = [(-1,0),(0,-1),(1,0),(0,1)]
        
        # Initial movement direction set to "up"
        self.moving_dir = "up"
        
        # Path and filename for the ghost's image based on color and direction
        self.img_path = f'assets/ghosts/{color}/'
        self.img_name = f'{self.moving_dir}_0.png'

        # Load and scale the ghost's image
        self.image = pygame.image.load(self.img_path + self.img_name)
        self.image = pygame.transform.scale(self.image, (CHAR_SIZE, CHAR_SIZE))

        # Update the rect attribute to match the image position
        self.rect = self.image.get_rect(topleft = (self.abs_x, self.abs_y))

        # Create a collision mask for precise collision detection
        self.mask = pygame.mask.from_surface(self.image)

        # Define possible directions for movement with their corresponding speeds
        self.directions = {
            'left': (-self.move_speed, 0), 
            'right': (self.move_speed, 0), 
            'up': (0, -self.move_speed), 
            'down': (0, self.move_speed)
        }
        
        # List of movement keys for easy reference
        self.keys = ['left', 'right', 'up', 'down']

        # Initial direction set to no movement
        self.direction = (0, 0)

        # Animation frame control
        self.frame = 0  # To alternate between two frames for each direction

    # Move the ghost back to its starting position
    def move_to_start_pos(self):
        self.rect.x = self.abs_x
        self.rect.y = self.abs_y

    # Check for collisions with walls
    def is_collide(self, x, y, walls_collide_list):
        # Create a temporary rectangle moved by (x, y)
        tmp_rect = self.rect.move(x, y)
        # Check if this new position collides with any wall; return True/False
        return tmp_rect.collidelist(walls_collide_list) != -1
    
    # Update the ghost's image based on its movement direction    
    def _animate(self):
        # Change the image file based on current direction
        self.frame = (self.frame + 1) % 2  # This will alternate between 0 and 1
        self.img_name = f'{self.moving_dir}_{self.frame}.png'  # Update image name based on the current direction and frame
        self.image = pygame.image.load(self.img_path + self.img_name)
        self.image = pygame.transform.scale(self.image, (CHAR_SIZE, CHAR_SIZE))
        # Update the rect to match the current image position
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

    # Update the ghost's movement and animation
    def update(self, walls_collide_list):
        # Determine valid movement options
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
            # Stop moving if collision occurs
            self.direction = (0,0)
        
        # teleporting to the other side of the map
        if self.rect.right <= 0:
            self.rect.x = WIDTH
        elif self.rect.left >= WIDTH:
            self.rect.x = 0

        # Update the animation
        self._animate()
