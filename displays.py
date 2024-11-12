# Class that will display game information, such as life, level, score, and game over message.

import pygame
from settings import WIDTH, HEIGHT, CHAR_SIZE

# Initialize pygame font module
pygame.font.init()

class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("assets/font/Joystix.TTF", CHAR_SIZE)          # Load the main font for displaying text
        self.game_over_font = pygame.font.Font("assets/font/Joystix.TTF", 48)       # Load a larger font for the game over message
        self.text_color = pygame.Color("black")                                     # Set the text color for rendering

    # Display the player's remaining lives on the screen.
    def show_life(self, life):
        img_path = "assets/life/life.png"
        life_image = pygame.image.load(img_path) 
        life_image = pygame.transform.scale(life_image, (CHAR_SIZE, CHAR_SIZE))     # Scale the life image to match character size
        life_x = CHAR_SIZE // 2                                                     # Initial x-coordinate for drawing life images
        if life != 0:
            for life in range(life):                                                # Iterate based on the number of lives
                self.screen.blit(life_image, (life_x, HEIGHT + (CHAR_SIZE // 2)))
                life_x += CHAR_SIZE                                                 # Iterate based on the number of lives
    
    # Display the current game level on the screen.
    def show_level(self, level):
        level_x = WIDTH // 3                                                        # x-coordinate for the level text
        level = self.font.render(f'Level {level}', True, self.text_color)
        self.screen.blit(level, (level_x, HEIGHT + (CHAR_SIZE // 2)))
    
    # Display the current score on the screen.
    def show_score(self, score):
        score_x = WIDTH // 3                                                        # x-coordinate for the score text
        score = self.font.render(f'{score}', True, self.text_color)
        self.screen.blit(score, (score_x * 2, (HEIGHT + (CHAR_SIZE // 2))))
    
    # Display the game over message and instruction to restart.
    def game_over(self):
        message_font = pygame.font.Font("assets/font/Joystix.TTF", 42)
        message = message_font.render(f'Game Over', True, pygame.Color("red"))

        instruction_font = pygame.font.Font("assets/font/Joystix.TTF", 20)
        instruction = instruction_font.render(f'Press "R" to Restart', True, pygame.Color("white"))
        
        # Get the rectangles to center text
        message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        instruction_rect = instruction.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Blit the message and instruction onto the screen
        self.screen.blit(message, message_rect)
        self.screen.blit(instruction, instruction_rect)


# The Display class is responsible for rendering game-related information on the screen,
# such as the player's remaining lives (show_life), current level (show_level), score (show_score),
# and game over message (game_over).       

        