import sys, pygame ,math
from Geo import *
from Blocks import *


def Rays(position , blocks,difBetweenAngles):
    raysList:list =[]
    for angle in range(0 , 360 , difBetweenAngles):
        direction = Vector2( math.sin( math.radians(angle)) , math.cos( math.radians(angle)) )
        raysList .append(Ray(position , direction).getEndPointLine(blocks))

    return raysList




if __name__ == '__main__':
    pygame.init()

    size = width, height = 1000, 1000
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    blocks = Blocks.GetBlocks(rand=True)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        mousePosition = pygame.mouse.get_pos()
        mousePosition = Point(mousePosition[0], mousePosition[1])
        screen.fill(black)

        rays = Rays(mousePosition , blocks,1)
        for i in rays:
            i.Draw(surface = screen , color =(255, 50,50 , 2))

        for block in blocks:
            block.Draw(surface=screen ,color =(255, 0,0 , 2) )
        pygame.display.flip()