#for pygame installation= http://askubuntu.com/questions/399824/how-to-install-pygame

import sys, pygame
import time
import os,sys
import pygame as pg #lazy but responsible (avoid namespace flooding)
from openid.extensions.ax import AXError
pygame.init()
size = width, height = 700, 600
speed = [2, 2]
red=   193, 235, 22
go=1
white = 255,255,255
black=255,0,253,2
clr=169,169,169
blue= 119, 51, 255 
pygame.display.set_caption(" Simple Game ! ! !") 
screen = pygame.display.set_mode(size)
castle = pygame.image.load("resources/images/ball.png")
x = 640
y = 100
step=40
a=0
b=0
c=0
d=0
e=0
f=0
ax=640
ay=100
bx=640
by=150
cx=640
cy=200
dx=640
dy=250
ex=640
ey=300
fx=640
fy=350
pygame.key.set_repeat(50, 50)
myfont = pygame.font.SysFont("monospace", 20)
myfont1 = pygame.font.SysFont("monospace", 35)

grass = pygame.image.load("resources/images/gras.png")
ar=[]
chance0=[20,56,325,60,600,60]
val=0


def point(self,val):
   

    label = myfont1.render(str("  !!! >>>>> GAME OVER <<<<<!!!"), 56, (0,55,0))
    label1 = myfont1.render(str(" Press END Button "), 56, (0,55,0))
    screen.blit(label, (100,100))
    screen.blit(label1, (140,140))
    pygame.QUIT
     
#     healthbar = pygame.image.load("resources/images/healthbar.png")

#     health = pygame.image.load("resources/images/health.png")
#     screen.blit(healthbar, (5,5))
#     for health1 in range(val):
#         screen.blit(health, (health1*6,18))
                


def progress(self,ax,ay,bx,by,cx,cy):
   # print "im in progress method"
    ch=0
    val=0
    chance=[[[20,56],[325,60],[600,60]],[[30,260],[326,260],[600,260]],[[30,460],[326,463],[600,460]],[[20,56],[30,260],[30,460]],[[325,60],[326,260],[326,463]],[[600,60],[600,260],[600,460]],[[20,56],[326,260],[600,460]],[[600,60],[326,260],[30,460]]]
   
    a=[ax,ay]
    b=[bx,by]
    c=[cx,cy]
   
    for c1 in chance:
         
      
        for i in range(0,len(c1)):
            if a==c1[i]:
                ch+=1
   
            if b==c1[i]:
                ch+=1
            if c==c1[i]:
                ch+=1
        if ch==3:
            val=1
            
            point(1,val)
            print "YOU GOT POINT ",ch
            
            ch=0
        else:
            ch=0         
def overlap(self,x,y):
     
    over_a=[x,y]
    over_b=[bx,by]
    overa=[ax,ay]
    over_c=[cx,cy]
    over_e=[dx,dy]
    overd=[ex,ey]
    over_f=[fx,fy]

    if over_a !=over_b and over_a!=over_c and over_a !=overa :
        if over_a !=over_e and over_a !=overd and over_a != over_f:
         return 1
   
        else:
            return 0
while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
                
        def bg(self):
            for xx in range(width/grass.get_width()+10):
                for yy in range(height/grass.get_height()+1):
                    screen.blit(grass,(xx*100,yy*100)) 
        def background(self):
            pygame.draw.line(screen, red, [30, 60], [600,60], 5)#first line horizontal
            pygame.draw.line(screen, red, [325, 60], [325,460], 5)
            pygame.draw.line(screen, red, [30, 260], [600,260], 5)
            pygame.draw.line(screen, red, [600, 460], [600,60], 5)
            pygame.draw.line(screen, red, [30, 60], [30,460], 5)
            pygame.draw.line(screen, red, [30, 460], [600,460], 5)
            # Circle
            pygame.draw.circle(screen, red, [31, 64], 10)
            label = myfont.render(str("1"), 56, (0,55,0))
            screen.blit(label, (31, 65))
            pygame.draw.circle(screen, red, [325, 64], 10)
            pygame.draw.circle(screen, red, [31, 262], 10)
            pygame.draw.circle(screen, red, [602, 462], 10)
            pygame.draw.circle(screen, red, [31, 462], 10)
            pygame.draw.circle(screen, red, [602, 62], 10)
            pygame.draw.circle(screen, red, [602, 262], 10)
            pygame.draw.circle(screen, red, [326, 462], 10)
            pygame.draw.circle(screen, red, [325, 262], 10)
        
        background(1)  
        
        def update_remaining(self):
         #A 
            #pygame.draw.rect(screen,black , ((ax, ay), (step, step)), 0)
            pygame.draw.circle(screen, black, [ax, ay], 20)
            #screen.blit(castle,(ax,ay))
            
            label = myfont.render(str("A"), ay+50, (0,55,0))
            screen.blit(label, (ax+8, ay+17))
         #B
            #pygame.draw.rect(screen,black , ((bx, by), (step, step)), 0)
            pygame.draw.circle(screen, black, [bx, by], 20)
            
            label = myfont.render(str("B"), by+50, (0,55,0))
            screen.blit(label, (bx+8, by+17)) 
          #C
           # pygame.draw.rect(screen,black , ((cx,cy), (step, step)), 0)
            pygame.draw.circle(screen, black, [cx, cy], 20)
            
            label = myfont.render(str("C"), cy+50, (0,55,0))
            screen.blit(label, (cx+8, cy+17)) 
          #D
            #pygame.draw.rect(screen,blue , ((dx,dy), (step, step)), 0)
            pygame.draw.circle(screen, blue, [dx, dy], 20)
            label = myfont.render(str("D"), dy+50, (0,55,0))
            screen.blit(label, (dx+8, dy+17)) 
          #E
            #pygame.draw.rect(screen,blue , ((ex,ey), (step, step)), 0)
            pygame.draw.circle(screen, blue, [ex, ey], 20)
           
            label = myfont.render(str("E"), ey+50, (0,55,0))
            screen.blit(label, (ex+8, ey+17))
          #F
            #pygame.draw.rect(screen,blue , ((fx,fy), (step, step)), 0)
            pygame.draw.circle(screen, blue, [fx,fy], 20)
           
            label = myfont.render(str("F"), fy+50, (0,55,0))
            screen.blit(label, (fx+8, fy+17))       
            
#~~~~~update_remaining(1)
        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print "a"
                a=1 
            elif event.key == pygame.K_b:
                print "b"
                b=1
                a=0
                
            elif event.key == pygame.K_c:
                print "c"
                c=1
                a=0
                b=0
            elif event.key == pygame.K_d:
                print "d"
                d=1
                c=0
                a=0
                b=0
            elif event.key == pygame.K_e:
                print "e"
                e=1
                d=0
                c=0
                a=0
                b=0
            elif event.key == pygame.K_f:
                print "f"
                f=1
                e=0
                d=0
                c=0
                a=0
                b=0
            if event.key == pygame.K_END :
                ax=640
                ay=100
                bx=640
                by=150
                cx=640
                cy=200
                dx=640
                dy=250
                ex=640
                ey=300
                fx=640
                fy=350
                screen.fill((0,0,0))
                pygame.display.update()
            if event.key == pygame.K_1:
                       x =20
                       y=56
                       screen.fill((0,0,0))
            if event.key == pygame.K_2:#20,56,326,260,600,460
                       x =325
                       y=60
                       screen.fill((0,0,0))
            if event.key == pygame.K_3:
                       x =600
                       y=60                    #600,60,600,260,600,460
                       screen.fill((0,0,0))           
            if event.key == pygame.K_4:   #30,260,326,260,600,260+20,56,30,260,30,460
                       x =30
                       y=260
                       screen.fill((0,0,0))           #600,60,326,260,30,460
            if event.key == pygame.K_5:
                       x =326
                       y=260
                       screen.fill((0,0,0))           
            if event.key == pygame.K_6:
                       x =600
                       y=260
                       screen.fill((0,0,0))    
            if event.key == pygame.K_7:
                       x =30  #325,60,326,260,326,463
                       y=460
                       screen.fill((0,0,0))           
                   
            if event.key == pygame.K_8:
                      x =326
                      y=463
                      screen.fill((0,0,0))           
            if event.key == pygame.K_9:
                       x =600
                       y=460
                        
                       screen.fill((0,0,0))           
             
        if a==1:
                    
            background(1)
            bg(1)
            over_result=overlap(1,x, y)
            if over_result==1:
                ax=x
                ay=y
            progress(1,ax,ay,bx,by,cx,cy)
            
            pygame.draw.rect(screen,clr , ((ax,ay), (step, step)), 0)
            label = myfont.render(str("A"), y+50, (0,55,0))
            #screen.blit(label, (ax+8, ay+17))
            update_remaining(1)
            pygame.display.update()
       
        elif b==1:
            
            over_result=overlap(1,x, y)
            if over_result==1:
                bx=x
                by=y
            background(1)
            bg(1)
            progress(1,ax,ay,bx,by,cx,cy)
            pygame.draw.rect(screen,clr , ((bx, by), (step, step)), 0)
            label = myfont.render(str("B"), y+50, (0,55,0))
            #screen.blit(label, (x+8, y+17))
            update_remaining(1)
            pygame.display.update()
        
        elif c==1:
         
            over_result=overlap(1,x, y)
            if over_result==1:
                cx=x
                cy=y
            progress(1,ax,ay,bx,by,cx,cy)
            background(1)
            bg(1)
            pygame.draw.rect(screen,clr , ((cx, cy), (step, step)), 0)
            label = myfont.render(str("C"), y+50, (0,55,0))
            screen.blit(label, (x+8, y+17))
             
            update_remaining(1)
            pygame.display.update()    
        
        elif d==1:
        
            over_result=overlap(1,x, y)
            if over_result==1:
                dx=x
                dy=y
            background(1)
            bg(1)
            progress(1,dx,dy,ex,ey,fx,fy)            

            pygame.draw.rect(screen,clr , ((dx, dy), (step, step)), 0)
            label = myfont.render(str("D"), y+50, (0,55,0))
            screen.blit(label, (x+8, y+17))
            update_remaining(1)
            pygame.display.update()    
        elif e==1:
            over_result=overlap(1,x, y)
            if over_result==1:
                ex=x
                ey=y
            background(1)
            bg(1)
            progress(1,dx,dy,ex,ey,fx,fy)            
            pygame.draw.rect(screen,clr , ((ex, ey), (step, step)), 0)
            label = myfont.render(str("E"), y+50, (0,55,0))
            screen.blit(label, (x+8, y+17))
             
            update_remaining(1)
            pygame.display.update()    
        elif f==1:
            over_result=overlap(1,x, y)
            if over_result==1:
                fx=x
                fy=y
            background(1)
            bg(1)
            progress(1,dx,dy,ex,ey,fx,fy)
            pygame.draw.rect(screen,clr , ((fx, fy), (step, step)), 0)
            label = myfont.render(str("F"), y+50, (0,55,0))
            screen.blit(label, (x+8, y+17))
            update_remaining(1)
            pygame.display.update()    
        