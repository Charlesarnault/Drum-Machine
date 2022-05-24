#Imports
import pygame
from pygame import mixer
from regex import R

pygame.init()

#Color params
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

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

#Functions
def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]

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

    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i+1)*100), (200, (i+1)*100), 3)

    for i in range(beats):
        for j in range(instruments):
            rect_x_ini = i*(WIDTH-200)//beats + 200
            rect_y_ini = j*100
            rect_width = (WIDTH-200)//beats
            rect_height = (HEIGHT-200)//instruments
            rect = pygame.draw.rect(screen, gray, [rect_x_ini, rect_y_ini, rect_width, rect_height], 5, 5)

#Main game loop
run = True

while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()

pygame.quit()