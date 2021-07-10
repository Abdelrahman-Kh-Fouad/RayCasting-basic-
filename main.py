import sys, pygame ,math
from Geo import *
from Blocks import *


def Rays(position , blocks,difBetweenAngles):
    raysList:list =[]
    angle =0
    while angle <=360 :
        direction = Vector2( math.sin( math.radians(angle)) , math.cos( math.radians(angle)) )
        raysList .append(Ray(position , direction).getEndPointLine(blocks))
        angle+=difBetweenAngles
    return raysList


if __name__ == '__main__':
    pygame.init()

    size = width, height = 1800, 1000
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    blocks = Blocks.GetBlocks(rand=True)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        mousePosition = pygame.mouse.get_pos()
        draw.circle(surface=screen , color=(255 ,255 ,255 ) , center=mousePosition , radius=1)

        mousePosition = Point(mousePosition[0], mousePosition[1])
        screen.fill(black)

        rays = Rays(mousePosition , blocks, 0.3 )
        for i in rays:
            i.Draw(surface = screen , color =(255, 255,255 , 2) , width=1 )

        for block in blocks:
            block.Draw(surface=screen ,color =(255, 0,0 , 2) , width=4 )
        pygame.display.flip()