import pygame, sys
from settings import WIDTH, HEIGHT, NAV_HEIGHT
from world import World

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_HEIGHT))
img = pygame.image.load("assets/pac/idle/0.png")

pygame.display.set_caption("Pac-Man")
pygame.display.set_icon(img)

# Load font
font = pygame.font.Font("assets/font/Joystix.TTF", 50)

# Render the text
# text_surface = font.render("Hello, Pac-Man!", True, (255, 255, 255))

#def render_text():
    # Function to render text onto the screen
    #screen.blit(text_surface, (100, 100))

# Load sound
chomp_sound = pygame.mixer.Sound("assets/audio/chomp.wav")
eat_ghost_sound = pygame.mixer.Sound("assets/audio/eatghost.wav")
eat_fruit_sound = pygame.mixer.Sound("assets/audio/eatfruit.wav")
death_sound = pygame.mixer.Sound("assets/audio/death.wav")
extra_life_sound = pygame.mixer.Sound("assets/audio/extrapac.wav")
beginning_sound = pygame.mixer.Sound("assets/audio/beginning.wav")

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.FPS = pygame.time.Clock()
    
    def main(self):
        world = World(self.screen)
        while True:
            #Fill the screen with a background color
            self.screen.fill("black")

            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Update and render the game world
            world.update()

            #Render the text on the screen
#            render_text()

            # Update the display
            pygame.display.update()
            self.FPS.tick(30)

if __name__ == "__main__":
    play = Main(screen)
    play.main()