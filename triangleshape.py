import pygame


class TriangleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,height,base):
        if hasattr(self,"containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.height = height
        self.base = base
        # self.area = (self.height*self.base)/2
        
    def draw(self,screen):
        pass
    
    def update(self,dt):
        pass

    def check_collision(self,other):
        # We check if any of the points of the triangle (Player object) are within the radius of Asteroid object
        for point in self.triangle():
            if (point.distance_to(other.position) < other.radius):
                return True
        return False