import pygame
import sys

pygame.init( )
disp = pygame.display.set_mode((650,500))
pygame.display.set_caption("Where to Put?")

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (255, 0, 0)
dark_red = (200, 0, 0)
gray = (211,211,211)
yellow = (255,255,0)

##Font
header = pygame.font.SysFont("Times New Roman", 18)
title = pygame.font.SysFont('Arial', 65)

def run( ):
    
    disp.fill(black)            
    live =  header.render('LIVE!!! LIVE!!! LIVE!!! LIVE!!! LIVE!!! LIVE!!!', 1,  yellow)
    disp.blit(live, (, 50))
    pygame.display.update( )
    
    while True:
        for event in pygame.event.get( ):
            if event.type == pygame.QUIT:
                pygame.quit( )
                sys.exit( )
     

run()

