import pymunk,pygame

class Sand:
    def __init__(self,space,color=(232, 222, 28)):
        self.space = space
        self.color = color
    
    def create(self,pos):
        body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body,(2,2))
        shape.friction = 15
        self.space.add(body,shape)

        return shape
    
    def draw(self,screen,sand):
        for particle in sand:
            pos_x = int(particle.body.position.x)
            pos_y = int(particle.body.position.y)
            pygame.draw.rect(screen,self.color,(pos_x,pos_y,2,2))