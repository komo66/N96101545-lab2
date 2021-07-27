import pygame
import time


# setup
WIN_WIDTH = 1024
WIN_HEIGHT = 600
FPS = 60
BLACK=(0,0,0)
RED=(255,0,0)
WHITE=(255,255,255)
HP=(40,40)
BUTTON=(80,80)
# initialization
pygame.init()
# create window surface
window=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# load images and change size
background=pygame.image.load('images/Map.png').convert()
enemy=pygame.image.load('images/enemy.png').convert()
enemy=pygame.transform.scale(enemy,(40,50))
enemy.set_colorkey(BLACK)
muse=pygame.image.load('images/muse.png').convert()
muse=pygame.transform.scale(muse,BUTTON)
pause=pygame.image.load('images/pause.png').convert()
pause=pygame.transform.scale(pause,BUTTON)
sound=pygame.image.load('images/sound.png').convert()
sound=pygame.transform.scale(sound,BUTTON)
be_continue=pygame.image.load('images/continue.png').convert()
be_continue=pygame.transform.scale(be_continue,BUTTON)
hp=pygame.image.load('images/hp.png').convert()
hp=pygame.transform.scale(hp,HP)
hp_gray=pygame.image.load('images/hp_gray.png').convert()
hp_gray=pygame.transform.scale(hp_gray,HP)
# set window caption
pygame.display.set_caption("My first game")
# clock
clock = pygame.time.Clock()
# game loop
run = True
while run:
    clock.tick(FPS)
    # event loop (user action)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # draw
    window.blit(background,(0,0))
    window.blit(enemy,(30,275))
    pygame.draw.rect(window,(RED),[25,270,50,5])
    pygame.draw.rect(window,(BLACK),[0,0,1024,80])
    window.blit(muse,(700,0))
    window.blit(sound,(780,0))
    window.blit(be_continue,(850,0))
    window.blit(pause,(930,0))
    for i in range(0,200,40):
        window.blit(hp,(400+i,0))
    for i in range(0,80,40):
        window.blit(hp,(400+i,40))
    for i in range(0,120,40):
        window.blit(hp_gray,(480+i,40))

   
    pygame.display.update()
# uninitialize all the pygame module
pygame.quit()

