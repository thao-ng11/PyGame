import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

while True:
     #create event loop to check for player i nput
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # run the sys module to close any running code
            #end while loop
            #must import first
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    # draw all our elements
    # update everything
    pygame.display.update() 
    clock.tick(60) #this is setting ceiling for frame rate 60fps