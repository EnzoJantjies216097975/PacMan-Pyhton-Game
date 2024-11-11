import pygame, sys
from settings import WIDTH, HEIGHT, NAV_HEIGHT
from world import World

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_HEIGHT))
pygame.display.set_caption("PacMan")

pygame.mixer.init()

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
            self.screen.fill("black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            world.update()
            pygame.display.update()
            self.FPS.tick(30)

if __name__ == "__main__":
    play = Main(screen)
    play.main()