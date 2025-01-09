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
        def point_circle_collision(vertice, other):
            return vertice.distance_to(other.position) < other.radius
        
        def edge_circle_collision(p1,p2,other):
            if point_circle_collision(p1, other) or point_circle_collision(p2, other):
                return True
            
            edge = p2 - p1
            dist_to_circle = other.position - p1
            projection = dist_to_circle.dot(edge) / edge.length_squared() * edge
            close_point = p1 + projection
            
            if (close_point - p1).dot(edge) < 0 or (close_point - p2).dot(edge) > 0:
                return False
            
            return point_circle_collision(close_point, other) 
        
        vertices = self.triangle()
        for i in range(3):
            p1 = vertices[i]
            p2 = vertices[(i+1)%3]
            if edge_circle_collision(p1,p2,other):
                return True
        
        return False