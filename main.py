# TODO: Add a scoring system
# TODO: Implement multiple lives and respawning
# TODO: Add an explosion effect for the asteroids
# TODO: Add acceleration to the player movement
# TODO: (optional) Make the objects wrap around the screen instead of disappearing
# TODO: (optional) Add a background image
# TODO: (optional) Add sound effects
# TODO: (optional) Add BGM
# TODO: Create different weapon types
# TODO: Make the asteroids lumpy instead of perfectly round
# TODO: Make the ship have a triangular hit box instead of a circular one
# TODO: Add a shield power-up
# TODO: Add a speed power-up
# TODO: Add bombs that can be dropped
# TODO: Add main menu and game over screens
# TODO: Add customization screen
# TODO: Add leveling system



import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    fpsClock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    
    asteroid_field = AsteroidField()
    
    Shot.containers = (updatable,drawable,shots)
    
    while(True):
        dt = fpsClock.tick(60)/1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt)
        
        for object in asteroids:
            if player.check_collision(object):
                print("Game over!")
                return
            # pass
        for object in asteroids:
            for bullet in shots:
                if object.check_collision(bullet):
                    object.split()
                    bullet.kill()
                    break
            
        screen.fill((0,0,0))
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
    

if __name__ == "__main__":
    main()