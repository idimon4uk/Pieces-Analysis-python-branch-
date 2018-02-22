import math
class Pies:
    x = 0
    y = 0
    z = 0
    index = 0
    def __init__(self,index_,x_, y_,z_):
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

    def getIndHeigh(isPiesA):
        ind1 = 0
        ind2 = 0
        range = 0.0
        i = 0
        while (i<len(claster)):
            j = i
            while (j < len(claster)):
                if(range < math.sqrt(math.pow(math.fabs(claster[i].x-claster[j].x),2)+math.pow(math.fabs(claster[i].z)-math.fabs(claster[j].z),2))):
                    ind1 = i
                    ind2 = j
                    range = math.sqrt(math.pow(math.fabs(claster[i].x-claster[j].x),2)+math.pow(math.fabs(claster[i].z)-math.fabs(claster[j].z),2))
                j+=1
            i+=1
        if (isPiesA):
            return ind1
        else:
            return ind2

    def getIndHeigh(isPiesA):
        ind1 = 0
        ind2 = 0
        range = 0.0
        i = 0
        while (i<len(claster)):
            j = i
            while (j < len(claster)):
                if(range < math.sqrt(math.pow(math.fabs(claster[i].x-claster[j].x),2)+math.pow(math.fabs(claster[i].y)-math.fabs(claster[j].y),2))):
                    ind1 = i
                    ind2 = j
                    range = math.sqrt(math.pow(math.fabs(claster[i].x-claster[j].x),2)+math.pow(math.fabs(claster[i].y)-math.fabs(claster[j].y),2))
                j+=1
            i+=1
        if (isPiesA):
            return ind1
        else:
            return ind2

        
    def size():
        return len(claster)

class couple_Pies :
    m = 0 #pies
    n = 0 # pies
    def __init__(self,m_,n_,mx,my,mz,nx,ny,nz):
        m = Pies(m_,mx,my,mz)
        n = Pies(n_,nx,ny,nz)
class Point:
    couple = []
    Particle = []
    agregates = []
    range = 3
    link = ""
    time = 0
    avgWidth = 0
    numAgregates = 0
    avgLength = 0
    avgS = 0

    def __init__(self):
        #parse
        print("init")
    
    def findCouple(self):
        arr = []
        i = 0
        while(i<len(arr)-1):
            j = i+1
            while(j<len(arr)):
                if(math.sqrt(math.pow(Particle[i].x-Particle[j].x,2)+math.pow(Particle[i].y-Particle[j].y,2)+math.pow(Particle[i].z-Particle[j].z,2))<=range):
                    arr.append(couple_Pies(i,j,Particle[i].x,Particle[i].y,Particle[i].z,Particle[j].x,Particle[j].y,Particle[j].z))
                j+=1
            i+=1
        return self.arr

    def clasterForm (self):
        clasters = []
        Piese_ = []
        Piese = []
        while (len(couple)!=0):
            isSorted = false
            i= 0
            while(i<len(couple)):
                intList = []
                intList.append(couple[0].m)
                intList.append(couple[0].n)
                del couple[0]
                isSorted = false
                while(isSorted==false):
                    isSorted = true
                    j = 0
                    while(j<len(couple)):
                        isSorted = true
                        k = 0
                        while(len(intList)>k):
                            if(couple[j].m.index==intList[k].index):
                                isSorted = false
                                isRepeat = false
                                l = 0
                                while(l<len(intList)):
                                    if(couple[j].n.index==intList[l].index):
                                        isRepeat = true
                                        break
                                    l+=1
                                if(isRepeat==false):
                                    intList.append(couple[j].n)
                                del couple[j]
                                j-=1
                                break
                            if(couple[j].n.index==intList[k].index):
                                isSorted = false
                                isRepeat = false
                                l = 0
                                while(l<len(intList)):
                                    if(couple[j].m.index==intList[l].index):
                                        isRepeat = true
                                        break
                                    l+=1
                                if(isRepeat==false):
                                    intList.append(couple[j].m)
                                del couple[j]
                                j-=1
                                break
                            k+=1
                        j+=1
                    
                Piese.append(intList)
                i+=1

        i=0
        while(i<len(Piese)):
            claster.append(Claster())
            j=0
            while(j<len(Piese[i])):
                claster[i].add(Piese[j])
                j+=1
            i+=1
        return self.clasters

