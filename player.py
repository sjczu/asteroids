import pygame
from triangleshape import TriangleShape
from circleshape import CircleShape
from constants import *

class Player(TriangleShape):
    timer = 0
    
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_SHAPE_HEIGHT,PLAYER_SHAPE_BASE)
        self.rotation = 0
        self.lives = PLAYER_BASE_LIVES
        self.score = PLAYER_BASE_SCORE
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.base / 2
        a = self.position + forward * self.height
        b = self.position - forward * self.height/2 - right
        c = self.position - forward * self.height/2 + right
        return [a, b, c]
    
    def respawn(self,x,y):
        self.rotation = 0
        self.lives -= 1
        super().__init__(self.x,self.y,PLAYER_SHAPE_HEIGHT,PLAYER_SHAPE_BASE)
        
    def draw(self,screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
        
    def update(self,dt):
        keys = pygame.key.get_pressed()
        
        self.timer -= dt
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot(dt)
                self.timer = SHOT_COOLDOWN
        if keys[pygame.K_q] and keys[pygame.K_LCTRL]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * SHOT_SPEED
        Shot(self.position.x, self.position.y, velocity)
        
        
class Shot(CircleShape):
    def __init__(self,x,y,velocity):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = velocity
    
    def draw(self,screen):
        pygame.draw.circle(screen, ("white"), self.position, self.radius)
        
    def update(self,dt):
        self.position += self.velocity * dt
        if self.position.x < 0 or self.position.x > SCREEN_WIDTH or self.position.y < 0 or self.position.y > SCREEN_HEIGHT:
            self.kill()