import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'Black') #if you don't work with pixel art you want True

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600

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
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos < -100: #allow the snail to move
        snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,250))
    # draw all our elements
    # update everything
    pygame.display.update() 
    clock.tick(60) #this is setting ceiling for frame rate 60fps