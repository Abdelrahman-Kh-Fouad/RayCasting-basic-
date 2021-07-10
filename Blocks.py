import random
from Geo import *
class Blocks :

    @classmethod
    def GetBlocks(cls , **kwargs )->list:
        if kwargs['rand']==True:
            blocks =[]
            for _ in range(random.randint(3, 5)):
                blocks.append(Line(Point( random.randint(0,1000) ,random.randint(0,1000) ) , Point( random.randint(0,1000) ,random.randint(0,1000) ) ))
        return blocks

