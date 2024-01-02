import pymunk,pygame

class Rectangle:
    def __init__(self,space,pos=[10,300]):
        self.space = space
        self.color = (208,213,217)
        self.pos = pos
        
    def create(self,size):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = self.pos
        shape = pymunk.Poly(body,size)
        shape.friction = 40
        self.space.add(body,shape)

        return shape
    
    def draw(self,screen,size):
        pygame.draw.rect(screen,self.color,pygame.Rect(self.pos[0]+10,self.pos[1]+10,size[1][0]-size[0][0],25))
