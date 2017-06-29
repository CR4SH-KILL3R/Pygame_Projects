import pygame
import random

pygame.init()
secure = random.SystemRandom()

def create_block(red,green,blue):
    background = pygame.Surface(screen.get_size())
    background.fill((red,green,blue))
    background = background.convert()
    return background

direction=[1,2,3,4]
positions = [100,150,200,250,300]
colors = [(255,0,0),(0,255,0),(0,0,255)]
screen = pygame.display.set_mode((640,480))
backBlock = create_block(0,0,0)
ball=[[100,100,1,secure.choice(colors)],[200,200,1,secure.choice(colors)]]
screen.blit(backBlock,(0,0))
mainloop = True
clock = pygame.time.Clock()
FPS = 30
playtime = 0.0
i=1
while mainloop:
    milliseconds = clock.tick(FPS)
    playtime += milliseconds/1000.0
    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
    pygame.display.set_caption(text)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Escape Key pressed")
                mainloop = False
    bb = create_block(0,0,0)
    if (i%10) == 0 and i < 1000:
        ball.append([secure.choice(positions),secure.choice(positions),1,secure.choice(colors)])
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
                pos[0] -= 1
                pos[1] -= 1
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
        pygame.draw.circle(bb,pos[3],(posX,posY),25)
        pos[2] = curr
    screen.blit(bb,(0,0))
    pygame.display.flip()
    i +=1

pygame.quit()
print("Pygame exit initiated")
