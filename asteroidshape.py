import pygame
import random
import math
from circleshape import CircleShape

class AsteroidShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.math.Vector2(x, y)
        self.vertices = []
        self.num_vertices = random.randrange(5, 10)
        self.angle_step = 360 / self.num_vertices
        for i in range(self.num_vertices):
            self.angle = self.angle_step * i
            self.vertex_x = self.x + self.radius * math.cos(self.angle)
            self.vertex_y = self.y + self.radius * math.sin(self.angle)
            self.vertices.append(pygame.math.Vector2(self.vertex_x, self.vertex_y))
    
    def draw(self,screen):
        pass
    
    def update(self,dt):
        pass

    # def check_collision(self,other):
    #     return self.position.distance_to(other.position) < self.radius + other.radius
    def check_collision(self, other):
        if isinstance(other, CircleShape):
            return self.position.distance_to(other.position) < self.radius + other.radius
        for vertex in self.vertices:
            if other.position.distance_to(vertex) < other.radius:
                return True
        for vertex in other.vertices:
            if self.position.distance_to(vertex) < self.radius:
                return True
        return False