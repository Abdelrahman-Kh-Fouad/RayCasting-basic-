from math import *
from copy import copy ,deepcopy
from pygame import Vector2 , draw
EPS = 1e-6  
class Point :
    def __init__(self , x , y ) -> None:
        self.x:float = x 
        self.y:float = y 

    def __add__(self , other):
        return Point(self.x + other.x , self.y + other.y )
    def __sub__(self , other):
        return Point(self.x - other.x , self.y - other.y )

    #Euclidean distance
    def distanceTo(self , to):
        return hypot((self.x - to.x) , (self.y - to.y))

    def ConvertToVector2(self):
        return Vector2(self.x , self.y)


#Linear eqution for line (ax + by - c = 0 ) 
class Line :
    def __init__(self , beginPoint:Point , endPoint:Point):
        self.beginPoint = beginPoint
        self.endPoint = endPoint
        self.direction = Vector2(endPoint.x - beginPoint.x , endPoint.y - beginPoint.y )


    def Draw(self , surface  , color ):
        draw.line(surface=surface , start_pos=self.beginPoint.ConvertToVector2() , end_pos=self.endPoint.ConvertToVector2() , color=color)

    # def __init__(self , firstPoint:Point , secondPoint:Point ) -> None:
    #     if fabs(firstPoint.x - secondPoint.x ) < EPS :
    #         self.a:float = 1
    #         self.b:float = 0
    #         self.c:float = -firstPoint.x
    #     else :
    #         self.a = -(firstPoint.y - secondPoint.y) /(firstPoint.x - secondPoint.x)
    #         self.b = 1.0
    #         self.c = -(self.a * firstPoint.x ) - firstPoint.y
        
    # def __init__(self , point :Point , slope : float) -> None:
    #     if slope > 1e16 :
    #         self.a = 1
    #         self.b = 0
    #         self.c:float = -point.x
    #
    #     else :
    #         self.a = -slope
    #         self.b = 1.0
    #         self.c = -(self.a * point.x ) - point.y


    # def areParallel(self , other) ->bool:
    #     return fabs(self.a - other.a < EPS) and fabs(self.b - other.b < EPS)
    #
    # def areSame(self , other)->bool:
    #     return self.areParallel(other) and fabs(self.c - other.c)<EPS
    def sameDirection(self , otherPoint:Point):
        otherDirction = Vector2(otherPoint.x - self.beginPoint.x , otherPoint.y - self.beginPoint.y )
        return otherDirction.normalize()==self.direction.normalize()

    def Intersection (self , other):
        x1 = self.beginPoint.x
        y1 = self.beginPoint.y

        x2 = self.endPoint.x
        y2 = self.endPoint.y

        x3 = other.beginPoint.x
        y3 = other.beginPoint.y

        x4 = other.endPoint.x
        y4 = other.endPoint.y

        den = (x1 -x2 )*(y3 - y4) - (y1 - y2)*(x3 -x4)

        if den == 0 :
            return False
        else :
            px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 -x2)*(x3*y4 - y3*x4))/den
            py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 -y2)*(x3*y4 - y3*x4))/den

            res =Point(px , py)
            if (self.sameDirection(res)):
                return res
            return False





class Ray :
    def __init__(self , position:Point , vec:Vector2 ) -> None:
        self.direction = deepcopy(vec)
        self.position = deepcopy(position)

    def changePosition(self , pos:Point):
        self.position = deepcopy(pos)

    def getEndPointLine(self , lines :list):

        res =Point(self.position.x + 2000* self.direction.x , self.position.y + 2000* self.direction.y )
        lineToInteract = Line(self.position , res)

        for line in lines :
            ret = lineToInteract.Intersection(line)
            if type(ret)!=bool:
                if ret.distanceTo(self.position) < res.distanceTo(self.position):
                    res = copy(ret)
        return Line(self.position , res)






        
    