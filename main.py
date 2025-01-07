import pygame
from constants import *

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # screen.set_caption("Asteroids")
    fpsClock = pygame.time.Clock()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        

if __name__ == "__main__":
    main()