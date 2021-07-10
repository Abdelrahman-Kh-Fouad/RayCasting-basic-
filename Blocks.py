import random
from Geo import *
class Blocks :
    def GetBlocks(  **kwargs )->list:
        if kwargs['rand']==True:
            blocks =[]
            for _ in range(random.randint(5, 10)):
                blocks.append(Line(Point( random.randint(0,1000) ,random.randint(0,1000) ) , Point( random.randint(0,1000) ,random.randint(0,1000) ) ))
        return blocks

