import pygame
import sys

pygame.init( )

disp = pygame.display.set_mode((650, 500))
pygame.display.set_caption("Where to Put?")

#Font
Title = pygame.font.Font('freesansbold.ttf', 30)
Person = pygame.font.Font("freesansbold.ttf", 20)
Talk = pygame.font.Font("freesansbold.ttf", 17)

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (255, 0, 0)
dark_red = (200, 0, 0)
champagne = (247, 231, 206)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect( )

def button(txt, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos( )
    
    if (x+w > mouse[0] > x) and (y + h > mouse [1] > y):
        pygame.draw.rect(disp, ac, (x, y,  w, h))
        textSurf, textRect = text_objects(txt, Talk)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        disp.blit(textSurf, textRect)
        return True
    
    else:
        pygame.draw.rect(disp, ic, (x, y,  w, h))
        textSurf, textRect = text_objects(txt, Talk)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        disp.blit(textSurf, textRect)

# ito yung nagpapadisplay sa text ng paisa isa
def display_text_animation(string):
    text = ''
    for i in range(len(string)): 
        text += string[i]
        text_surface = Talk.render(text, 0, black)
        disp.blit(text_surface, (30,405))
        pygame.display.update()
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

#ito yung nagbliblit kung sino nagsasalita at ano sinasabi niya
def mainframe(speaker, dialogue):
    ctr = 0
    mouse = pygame.mouse.get_pos( )
    pygame.draw.rect(disp, (255,255,255), (15,350,620,135))                
    Character =  Person.render(speaker, 1,  black)
    Dialogue =  Talk.render(dialogue, 0,  black)
    disp.blit(Character, (30,365))
    #this loop makes sure that the function is only called once
    while ctr == 0:
        display_text_animation(dialogue)
        ctr +=1    
    disp.blit(Dialogue, (30,405))
    pygame.display.update()

def mainframe_two(speaker, dialogue):
    ctr = 0
    mouse = pygame.mouse.get_pos( )
    pygame.draw.rect(disp, (255,255,255), (15,350,620,135))                
    Character =  Title.render(speaker, 1,  white)
    Dialogue =  Person.render(dialogue, 1,  white)
    disp.blit(Character, (30,365))
    disp.blit(Dialogue, (30,405))
    pygame.display.update
    