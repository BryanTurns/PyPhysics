from utils import randomFillMulti
from physics import update_entities, calculateRadius, update_entities_multi
from const import WINDOW_HEIGHT, WINDOW_WIDTH, QUANTITY, MAX_MASS, FRAMERATE, BASE_DT
import pygame
import math

# Determines rate that sim changes
global dt 
global fps
dt = BASE_DT
fps = 0

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# [m, x, y, vx, vy, r]
entityList = randomFillMulti(QUANTITY, MAX_MASS)



def main():
    global fps

    clock = init()
    i = 0
    while True:
        
        event = processInput()
        if event == pygame.QUIT:
            break
        
        result = update_entities_multi(entityList, dt)
        while result != 0:
            result = update_entities_multi(entityList, dt)

        render()      

        t = clock.tick(FRAMERATE)
        if i % 30 == 0:
            fps = 1000.0/t
        i += 1
    return 0


def init():
    clock = pygame.time.Clock()
    
    print(entityList)
    for entity in entityList:
        entity[5] = calculateRadius(entity[0])
    return clock


def processInput():
    global dt
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                dt -= 0.1
                print(dt)
            elif event.key == pygame.K_UP:
                dt += 0.1
                print(dt)
        
        if event.type == pygame.QUIT:
            pygame.quit()

    return  


def render():
    for entity in entityList:
        if entity[6] == 0:
            pygame.draw.circle(window, (0, 0, 255), (entity[1], entity[2]), entity[5])
        elif entity[6] == 1:
            pygame.draw.circle(window, (0, 255, 0), (entity[1], entity[2]), entity[5])
        elif entity[6] == 2:
            pygame.draw.circle(window, (255, 0, 0), (entity[1], entity[2]), entity[5])

    text_surface = my_font.render(str(math.floor(fps)), False, (155, 0, 0))
    window.blit(text_surface, (0, 0))

    pygame.display.update()
    window.fill((0,0,0))
    pass

# def render(fps):


if __name__ == "__main__":
    main()
