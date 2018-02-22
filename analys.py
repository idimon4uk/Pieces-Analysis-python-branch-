import math
class Pies:
    x = 0
    y = 0
    z = 0
    index = 0
    def __init__(self,x_, y_,z_,index_):
        self.x=x_
        self.y=y_
        self.z=z_
        self.index = index_


class Claster:
    r = 0 #radius of sphere
    claster = []
    
    def add (self,pies):
        claster.append(pies)
    
    def analys(self):
        return s(claster[getInd(true)],claster[getInd(false)])
    
    def s(a,b):
        d = radius(a,b)
        return math.pi * math.pow((d+r),2)

    def radius(a,b):
        return math.sqrt(math.pow(math.fabs(a.x-b.x),2)+math.pow(math.fabs(a.y-b.y),2))/2

    def heigh(a,b):
        return math.sqrt(math.pow(math.fabs(a.x-b.x),2)+math.pow(math.fabs(a.z-b.z),2))

    def s_Full():
        return 2*math.pi * radius(claster[getInd(true)],claster[getInd(true)])*heigh(claster[getIndHeigh(true)],claster[getIndHeigh(true)])








    

