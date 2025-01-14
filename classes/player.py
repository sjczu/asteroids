import pygame
from classes.triangleshape import TriangleShape
from classes.circleshape import CircleShape
from config.settings import PLAYER_SHAPE_HEIGHT, PLAYER_SHAPE_BASE, PLAYER_BASE_LIVES, PLAYER_BASE_SCORE, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_COOLDOWN, SHOT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS, PLAYER_BASE_ACCELERATION
from config.stats import *
import config.items

class Player(TriangleShape):
    timer = 0
    
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_SHAPE_HEIGHT,PLAYER_SHAPE_BASE)
        self.rotation = 0
        self.lives = PLAYER_BASE_LIVES
        self.score = PLAYER_BASE_SCORE
        self.total_score = PLAYER_TOTAL_SCORE
        self.accelerating = None
        # self.__shield = None
        # self.__thruster = None
        # self.__weapon = None
    
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
        super().__init__(x,y,PLAYER_SHAPE_HEIGHT,PLAYER_SHAPE_BASE)
        
    def draw(self,screen):
        # if self.__shield is None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        # else:
        #     pygame.draw.polygon(screen, "white", self.triangle(), 2)
        #     points = self.triangle()
        #     points = [point + pygame.Vector2(2, 2) for point in points]
        #     pygame.draw.polygon(screen, "blue", points, 4)
        
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
            self.accelerating = True
        elif keys[pygame.K_s]:
            self.accelerating = False
            # self.move(-dt,self.accelerating)
        else: 
            self.accelerating = None
        
        self.move(dt,self.accelerating)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot(dt)
                self.timer = SHOT_COOLDOWN
        if keys[pygame.K_q] and keys[pygame.K_LCTRL]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            
    def move(self, dt, accelerating):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        backward = -forward
        if accelerating is True:
            self.velocity += forward * PLAYER_BASE_ACCELERATION * dt
            if self.velocity.length() > PLAYER_SPEED:
                self.velocity.scale_to_length(PLAYER_SPEED)
        elif accelerating is False:
            self.velocity += backward * PLAYER_BASE_ACCELERATION * dt # * 0.5?
            if self.velocity.length() > PLAYER_SPEED:
                self.velocity.scale_to_length(PLAYER_SPEED)
        else:
            friction = PLAYER_BASE_ACCELERATION * dt * 0.5
            if self.velocity.length() > friction:
                self.velocity -= self.velocity.normalize() * friction
            else:
                self.velocity = pygame.Vector2(0, 0)
        
        self.position += self.velocity * dt
    
    def shoot(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * SHOT_SPEED
        Shot(self.position.x, self.position.y, velocity)
        
    def add_score(self,other):
        self.score += other.points
        
        
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