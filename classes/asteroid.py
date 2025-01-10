import pygame
from classes.asteroidshape import AsteroidShape
from config.settings import ASTEROID_BASE_SCORE, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
import random
import math

class Asteroid(AsteroidShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0,0)
        self.rotation = 0

        self.points = ASTEROID_BASE_SCORE * (self.radius / ASTEROID_MAX_RADIUS)
        
    def draw(self,screen):
        pygame.draw.polygon(screen, "white", [(vertex.x, vertex.y) for vertex in self.vertices], 2)
        
    
    def update(self,dt):
        self.position += self.velocity * dt
        self.rotation += 1
        
        # Recalculate vertices based on current position and rotation in order to draw the rotating asteroids
        angle_step = 360 / len(self.vertices)
        for i, vertex in enumerate(self.vertices):
            angle = math.radians(angle_step * i + self.rotation)
            distance = self.radius 
            vertex.x = self.position.x + distance * math.cos(angle)
            vertex.y = self.position.y + distance * math.sin(angle)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        
        asteroid1.velocity = self.velocity.rotate(random.uniform(20,50))*1.2
        asteroid2.velocity = self.velocity.rotate(-(random.uniform(20,50)))*1.2