#Imports
import pygame
from pygame import mixer
from regex import R

pygame.init()

#Color params
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
red = (255, 0, 0)
gold = (212, 175, 155)

#Screen params
WIDTH = 1400
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('freesansbold.ttf', 28)

#Time params
fps = 60
timer = pygame.time.Clock()
instruments = 6
beats = 8

#Other variables
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

#Functions
def draw_grid(clicks):
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    colors = [gray, white, gray]
    boxes = []
    
    #Hi Hat
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    #Snare
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    #Bass Drum
    bass_drum_text = label_font.render('Bass Drum', True, white)
    screen.blit(bass_drum_text, (30, 230))
    #Crash
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 330))
    #Clap
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    #Floor Tom
    floor_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_text, (30, 530))

    #Creating the instruments grid
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i+1)*100), (200, (i+1)*100), 3)

    #Creating the boxes grid
    for i in range(beats):
        for j in range(instruments):
            
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            
            rect_x_ini = i*(WIDTH-200)//beats + 200
            rect_y_ini = j*100
            rect_width = (WIDTH-200)//beats
            rect_height = (HEIGHT-200)//instruments

            rect = pygame.draw.rect(screen, color, [rect_x_ini+5, rect_y_ini+5, rect_width - 10, rect_height - 10], 0, 3)
            pygame.draw.rect(screen, gold, [rect_x_ini, rect_y_ini, rect_width, rect_height], 5, 5)
            pygame.draw.rect(screen, black, [rect_x_ini, rect_y_ini, rect_width, rect_height], 2, 5)
            
            boxes.append((rect, (i,j)))

    return boxes

#Main game loop
run = True

while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                if box[0].collidepoint(event.pos):
                    coords = box[1]
                    clicked[coords[1]][coords[0]] *= -1
        
    pygame.display.flip()

pygame.quit()