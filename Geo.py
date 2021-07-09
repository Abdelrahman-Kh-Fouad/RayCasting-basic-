from math import * 
from pygame import Vector2
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





#Linear eqution for line (ax + by - c = 0 ) 
class Line :
    def __init__(self , firstPoint:Point , secondPoint:Point ) -> None:
        if fabs(firstPoint.x - secondPoint.x ) < EPS :
            self.a:float = 1 
            self.b:float = 0
            self.c:float = -firstPoint.x
        else :
            self.a = -(firstPoint.y - secondPoint.y) /(firstPoint.x - secondPoint.x)
            self.b = 1.0
            self.c = -(self.a * firstPoint.x ) - firstPoint.y
        
    def __init__(self , point :Point , slope : float) -> None:
        if slope > 1e16 :
            self.a = 1
            self.b = 0
            self.c:float = -point.x

        else :
            self.a = -slope
            self.b = 1.0
            self.c = -(self.a * point.x ) - point.y


    def areParallel(self , other) ->bool:
        return fabs(self.a - other.a < EPS) and fabs(self.b - other.b < EPS)

    def areSame(self , other)->bool:
        return self.areParallel(other) and fabs(self.c - other.c)<EPS

    def Intersection (self , other):
        

        

class Ray :
    def __init__(self , vec:Vector2 ) -> None:
        self.direction=vec

    def 

        
    