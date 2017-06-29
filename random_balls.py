"""
This is a PyGame application Developed by Fahim Karim
Last Update -- 29.06.2017 @ 1:45 PM (IST)
"""
import pygame
import random

pygame.init()
#for crytographically secure random
secure = random.SystemRandom()

#function for generating surface of a given color
def create_block(red,green,blue):
    background = pygame.Surface(screen.get_size())
    background.fill((red,green,blue))
    background = background.convert()
    return background

#directions list
direction=[1,2,3,4,2,3,4]
#positions list
positions = [100,150,200,250,300]
#colors list
colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]

#setting up the screen
screen = pygame.display.set_mode((640,480))
backBlock = create_block(0,0,0)
ball=[[100,100,1,secure.choice(colors)],[200,200,1,secure.choice(colors)]]
screen.blit(backBlock,(0,0))
#for mainloop
mainloop = True

#for showing fps and up-time
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0

i=1

while mainloop:
    #displaying the fps and playtime
    milliseconds = clock.tick(FPS)
    playtime += milliseconds/1000.0
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)

    #to exit the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Escape Key pressed")
                mainloop = False
    #surface onto which everything will be drawn
    bb = create_block(0,0,0)
    #background pattern
    for point in range(0,641,20):
        pygame.draw.line(bb,(255,0,0),(0,0),(point,480),1)
    for point in range(0,481,20):
        pygame.draw.line(bb,(0,0,255),(640,0),(0,point),1)
    for point in range (0,480,20):
        pygame.draw.line(bb,(0,255,0),(0,480),(640,point),1)
    for point in range(0,640,20):
        pygame.draw.line(bb,(255,255,0),(640,480),(point,0),1)

    #to add balls after intervals    
    if (i%10) == 0 and i < 1000:
        ball.append([secure.choice(positions),secure.choice(positions),1,secure.choice(colors)])

    #balls and their movements
    for pos in ball:
        posX = pos[0]
        posY = pos[1]
        curr = pos[2]
        if posX == 100 and posY == 100:
            direc=secure.choice(direction)
            if (direc == 1):
                pos[0] += 3
                pos[1] += 3
                curr=1
            elif (direc == 2):
                pos[0] += 3
                pos[1] -= 3
                curr=2
            elif (direc == 3):
                pos[0] -= 3
                pos[1] -= 3
                curr=3
            elif (direc == 4):
                pos[0] -= 3
                pos[1] += 3
                curr=4
        elif posX >= 610:
            if curr==2:
                pos[0] -=3
                pos[1] -=3
                curr=3
            else:
                pos[0] -= 3
                pos[1] += 3
                curr=4
        elif posY <= 25:
            if curr==3:
                pos[0] -= 3
                pos[1] +=3
                curr=4
            else:
                pos[0] +=3
                pos[1] +=3
                curr=1
        elif posX <= 25:
            if curr == 4:
                pos[0] += 3
                pos[1] +=3
                curr=1
            else:
                pos[0] +=3
                pos[1] -=3
                curr=2
        elif posY >= 448:
            if curr==1:
                pos[0] += 3
                pos[1] -= 3
                curr=2
            else:
                pos[0] -= 3
                pos[1] -= 3
                curr=3
        else:
            if curr == 1:
                pos[0] +=3
                pos[1] += 3
            elif curr == 2:
                pos[0] += 3
                pos[1] -= 3
            elif curr == 3:
                pos[0] -= 3
                pos[1] -= 3
            elif curr == 4:
                pos[0] -= 3
                pos[1] += 3
        #draw the ball to the surface
        pygame.draw.circle(bb,pos[3],(posX,posY),25)
        pos[2] = curr
    #blitting and refreshing the screen
    screen.blit(bb,(0,0))
    pygame.display.flip()
    i +=1

pygame.quit()
print("Pygame exit initiated")
