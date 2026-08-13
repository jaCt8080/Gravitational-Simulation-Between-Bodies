import sys
import pygame
import random
from features import Body

WIDTH,HEIGHT=1500,750
surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Gravitational Simulation")
clock=pygame.time.Clock()

Bodies=[]
for _ in range(2):
    Color=(random.randint(125,225),random.randint(125,225),random.randint(125,225))
    Radius=random.randint(20,35)
    Mass= Radius**3
    X_pos=random.randint(Radius,WIDTH-Radius)
    Y_pos=random.randint(Radius,HEIGHT-Radius)
    X_vel=random.choice([-4,-3,-2,2,3,4])
    Y_vel=random.choice([-4,-3,-2,2,3,4])
    Bodies.append(Body(Color,Radius,X_pos,Y_pos,X_vel,Y_vel,Mass))

running = True
while running:
    surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        
    for i in Bodies:
        i.movement(WIDTH,HEIGHT)
    for i in range(len(Bodies)):
        for j in range(i+1,len(Bodies)):
            Bodies[i].gravity(Bodies[j])
    for i in range(len(Bodies)):
        for j in range(i+1,len(Bodies)):
            Bodies[i].collision(Bodies[j])
    for i in Bodies:
        i.visual(surface)

    pygame.display.flip()
    clock.tick(90) 
pygame.quit()
sys.exit()