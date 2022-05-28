#Imports
import pygame
from pygame import mixer
from regex import R

pygame.init()

### Initializing ###

#Color params
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (64, 64, 64)
green = (0, 255, 0)
red = (255, 0, 0)
gold = (212, 175, 155)
cyan = (0, 255, 255)

#Screen params
WIDTH = 1400
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('freesansbold.ttf', 28)
medium_font = pygame.font.Font('freesansbold.ttf', 22)

#Time params
fps = 60
timer = pygame.time.Clock()
instruments = 6
beats = 8
bpm = 240

#Game params
playing = True
active_length = 0
active_beat = 1
beat_changed = True
active_list = [1 for _ in range(instruments)]

#Other variables
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]

#Loading sounds
hi_hat = mixer.Sound('./sounds/hi_hat.WAV')
snare = mixer.Sound('./sounds/snare.WAV')
bass = mixer.Sound('./sounds/kick.WAV')
crash = mixer.Sound('./sounds/crash.wav')
clap = mixer.Sound('./sounds/clap.wav')
floor = mixer.Sound('./sounds/tom.WAV')
pygame.mixer.set_num_channels(instruments * 3)

### Computing useful functions ###

def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i==0:
                hi_hat.play()
            elif i==1:
                snare.play()
            elif i==2:
                bass.play()
            elif i==3:
                crash.play()
            elif i==4:
                clap.play()
            elif i==5:
                floor.play()

def draw_grid(clicks, beat, active_instruments):
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    colors = [gray, white, gray]
    boxes = []
    
    #Hi Hat
    hi_hat_text = label_font.render('Hi Hat', True, colors[active_instruments[0]])
    screen.blit(hi_hat_text, (30, 30))
    #Snare
    snare_text = label_font.render('Snare', True, colors[active_instruments[1]])
    screen.blit(snare_text, (30, 130))
    #Bass Drum
    bass_drum_text = label_font.render('Bass Drum', True, colors[active_instruments[2]])
    screen.blit(bass_drum_text, (30, 230))
    #Crash
    crash_text = label_font.render('Crash', True, colors[active_instruments[3]])
    screen.blit(crash_text, (30, 330))
    #Clap
    clap_text = label_font.render('Clap', True, colors[active_instruments[4]])
    screen.blit(clap_text, (30, 430))
    #Floor Tom
    floor_text = label_font.render('Floor Tom', True, colors[active_instruments[5]])
    screen.blit(floor_text, (30, 530))

    #Creating the instruments grid
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i+1)*100), (200, (i+1)*100), 3)

    #Creating the boxes grid
    for i in range(beats):
        for j in range(instruments):
            
            if clicks[j][i] == -1:
                color = gray
            elif active_instruments[j] == -1:
                color = dark_gray
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

        active = pygame.draw.rect(screen, cyan, [beat*(WIDTH-200)//beats + 200, 0, ((WIDTH-200)//beats), instruments*100], 5, 3)

    return boxes

### Main game loop ###

run = True

while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat, active_list)

    #Lower menu buttons

    play_pause_btn = pygame.draw.rect(screen, gray, [50, HEIGHT-150, 200, 100], 0, 5)
    play_pause_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_pause_text, (70, HEIGHT - 130))

    if playing:
        playing_status_text = medium_font.render('Playing', True, dark_gray)
    else:
        playing_status_text = medium_font.render('Paused', True, dark_gray)
    screen.blit(playing_status_text, (70, HEIGHT - 100))

    #bpm

    bpm_rect = pygame.draw.rect(screen, gray, [300, HEIGHT - 150, 200, 100], 5, 5)
    bpm_text = medium_font.render('Beats per minute', True, white)
    screen.blit(bpm_text, (308, HEIGHT - 130))
    bpm_text_2 = label_font.render(f'{bpm}', True, white)
    screen.blit(bpm_text_2, (370, HEIGHT - 100))

    bpm_add_rect = pygame.draw.rect(screen, gray, [510, HEIGHT-150, 48, 48], 0, 5)
    bpm_sub_rect = pygame.draw.rect(screen, gray, [510, HEIGHT-100, 48, 48], 0, 5)
    add_text = medium_font.render('+5', True, white)
    sub_text = medium_font.render('-5', True, white)
    screen.blit(add_text, (520, HEIGHT - 140))
    screen.blit(sub_text, (520, HEIGHT - 90))

    #Beats in one loop

    beats_rect = pygame.draw.rect(screen, gray, [600, HEIGHT - 150, 200, 100], 5, 5)
    beats_text = medium_font.render('Beats per minute', True, white)
    screen.blit(beats_text, (618, HEIGHT - 130))
    beats_text_2 = label_font.render(f'{bpm}', True, white)
    screen.blit(beats_text_2, (680, HEIGHT - 100))

    beats_add_rect = pygame.draw.rect(screen, gray, [810, HEIGHT-150, 48, 48], 0, 5)
    beats_sub_rect = pygame.draw.rect(screen, gray, [810, HEIGHT-100, 48, 48], 0, 5)
    beats_add_text = medium_font.render('+1', True, white)
    beats_sub_text = medium_font.render('-1', True, white)
    screen.blit(beats_add_text, (820, HEIGHT - 140))
    screen.blit(beats_sub_text, (820, HEIGHT - 90))

    #Instrument rects

    instrument_rects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i*100), (200, 100))
        instrument_rects.append(rect)
    
    #Save and Load rects

    save_rect = pygame.draw.rect(screen, gray, [900, HEIGHT-150, 200, 48], 0, 5)
    save_text = label_font.render('Save', True, white)
    screen.blit(save_text, (910, HEIGHT-140))
    load_rect = pygame.draw.rect(screen, gray, [900, HEIGHT-100, 200, 48], 0, 5)
    load_text = label_font.render('Load', True, white)
    screen.blit(load_text, (910, HEIGHT-90))

    #Clear board rect

    clear_rect = pygame.draw.rect(screen, gray, [1150, HEIGHT-150, 200, 100], 0, 5)
    clear_text = label_font.render('Clear board', True, white)
    screen.blit(clear_text, (1160, HEIGHT-120))

    #Playing sounds on beat changes

    if beat_changed:
        play_notes()
        beat_changed = False

    #Handling user clicks

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                if box[0].collidepoint(event.pos):
                    coords = box[1]
                    clicked[coords[1]][coords[0]] *= -1

        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause_btn.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True
            elif bpm_add_rect.collidepoint(event.pos):
                bpm += 5
            elif bpm_sub_rect.collidepoint(event.pos):
                bpm -= 5
            elif beats_add_rect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beats_sub_rect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            elif clear_rect.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
            
            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1
            


    beat_length = 3600/bpm

    #Handling beat changes

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True
       
    pygame.display.flip()

pygame.quit()