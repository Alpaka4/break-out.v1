import pygame
import sys
from config_2 import *
from bat_br import Bat
from ball_br import Ball
from brick import Brick
def point_in_rect(px,py,rect_x,rect_y,rect_w,rect_h):
    inx=rect_x<=px<=rect_x+rect_w 
    iny=rect_y<=py<=rect_y+rect_h
    return inx and iny
ORANGE = (255,155,100)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
YELLOW = (255,180,0)
bat_br=Bat()
ball_br=Ball()
brick=Brick()
clock = pygame.time.Clock()
sc = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    bat_br.update()
    ball_br.update()

    if ball_br.r>=brick.y-ball_br.r:
        ball_br.speeed_y+=-ball_br.speed_y

    mid_leftx=ball_br.x-ball_br.r
    mid_lefty=ball_br.y
     
    mid_rightx=ball_br.x+ball_br.r
    mid_righty=ball_br.y
     
    mid_topx=ball_br.x
    mid_topy=ball_br.y-ball_br.r
     
    mid_bottomx=ball_br.x
    mid_bottomy=ball_br.y+ball_br.r
    #верхняя граница ракетки №1
    if point_in_rect(mid_bottomx,mid_bottomy,bat_br.x,bat_br.y,BAT_WIDTH,BAT_HEIGHT):
        ball_br.speed_y=-ball_br.speed_y 



    sc.fill(BLACK)
    pygame.draw.rect(sc, WHITE,(bat_br.x,bat_br.y,BAT_WIDTH,BAT_HEIGHT))
    pygame.draw.circle(sc, ORANGE,(ball_br.x, ball_br.y), ball_br.r)
    pygame.draw.rect(sc, YELLOW,(brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT))



    pygame.display.update()


    clock.tick(FPS)
