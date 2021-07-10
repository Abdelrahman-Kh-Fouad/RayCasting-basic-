import sys, pygame ,math
from Geo import *


def Rays(position , difBetweenAngles):
    raysList:list =[]
    for angle in range(0 , 360 , difBetweenAngles):
        direction = Vector2( math.sin( math.radians(angle)) , math.cos( math.radians(angle)) )
        raysList .append(Ray(position , direction).getEndPointLine([]))

    return raysList

if __name__ == '__main__':
    pygame.init()

    size = width, height = 1000, 1000
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        mousePosition = pygame.mouse.get_pos()
        mousePosition = Point(mousePosition[0], mousePosition[1])
        screen.fill(black)

        rays = Rays(mousePosition , 1)
        for i in rays:
            i.Draw(surface = screen , color =(255, 255,255))
        pygame.display.flip()