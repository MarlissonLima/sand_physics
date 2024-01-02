import pygame,pymunk,sys
from sand import Sand
from rectangle import Rectangle
pygame.init()
win_size = (400,400)
screen  = pygame.display.set_mode(win_size)

pygame.display.set_caption('Sand simulation')
clock = pygame.time.Clock()
FPS = 120

space = pymunk.Space()
space.gravity = (0,100)

sand_particles_yellow = []
sand_particles_blue = []
sand = Sand(space)
sandB = Sand(space,color=(28, 147, 232))

rectangle = Rectangle(space)
horizontal_size =[[10,10],[350,10],[350,60],[10,60]]
rectangle.create(horizontal_size)




mouse_buttom = False
switch_color_key = False

while True:
    screen.fill('black')

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_buttom=True
        if event.type==pygame.MOUSEBUTTONUP:
            mouse_buttom=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                switch_color_key=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_q:
                switch_color_key=False

    if (mouse_buttom==True and switch_color_key==False):
        sand_particles_yellow.append(sand.create(event.pos))
    if (switch_color_key==True):
        sand_particles_blue.append(sandB.create(pygame.mouse.get_pos()))

    
    rectangle.draw(screen,horizontal_size)
    sand.draw(screen,sand_particles_yellow)
    sandB.draw(screen,sand_particles_blue)

    
    

    space.step(1/50)
    pygame.display.update()
    clock.tick(FPS)

