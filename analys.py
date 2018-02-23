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
    def __init__(self):
        self.claster = []

    def add (self,pies):
        self.claster.append(pies)
    
    def analys(self):
        return s(self.claster[self.getInd(true)],self.claster[self.getInd(false)])
    
    def s(a,b):
        d = self.radius(a,b)
        return math.pi * math.pow((d+self.r),2)

    def radius(a,b):
        return (math.sqrt(math.pow(math.fabs(a.x-b.x),2)+math.pow(math.fabs(a.y-b.y),2))/2)

    def heigh(a,b):
        return math.sqrt(math.pow(math.fabs(a.x-b.x),2)+math.pow(math.fabs(a.z-b.z),2))

    def s_Full():
        return 2*math.pi * radius(self.claster[getInd(true)],self.claster[getInd(true)])*heigh(self.claster[getIndHeigh(true)],self.claster[getIndHeigh(true)])

    def getIndHeigh(isPiesA):
        ind1 = 0
        ind2 = 0
        range = 0.0
        i = 0
        while (i<len(self.claster)):
            j = i
            while (j < len(self.claster)):
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
    range = 3
    link = ""
    time = 0
    avgWidth = 0
    numAgregates = 0
    avgLength = 0
    avgS = 0
    time = 0

    def __init__(self,len,es):
        k = 0
        self.couple = []
        self.Particle = []
        self.agregates = []
        while (k < len):
            self.Particle.append(Pies(k,es.part[k].pos[0],es.part[k].pos[1],es.part[k].pos[2]))
            k+=1
        self.couple = self.findCouple()
        self.agregates = self.clasterForm()
        print(self.agregates)
    
    def findCouple(self):
        self.arr = []
        i = 0
        while(i<len(self.arr)-1):
            j = i+1
            while(j<len(self.arr)):
                if(math.sqrt(math.pow(self.Particle[i].x-self.Particle[j].x,2)+math.pow(self.Particle[i].y-self.Particle[j].y,2)+math.pow(self.Particle[i].z-self.Particle[j].z,2))<=range):
                    self.arr.append(couple_Pies(i,j,self.Particle[i].x,self.Particle[i].y,self.Particle[i].z,self.Particle[j].x,self.Particle[j].y,self.Particle[j].z))
                j+=1
            i+=1
        return self.arr

    def clasterForm (self):
        self.clasters = []
        self.Piese_ = []
        self.Piese = []
        while (len(self.couple)!=0):
            isSorted = False
            i= 0
            while(i<len(self.couple)):
                intList = []
                intList.append(self.couple[0].m)
                intList.append(self.couple[0].n)
                del self.couple[0]
                isSorted = False
                while(isSorted==False):
                    isSorted = True
                    j = 0
                    while(j<len(self.couple)):
                        isSorted = True
                        k = 0
                        while(len(intList)>k):
                            if(self.couple[j].m.index==intList[k].index):
                                isSorted = False
                                l = 0
                                while(l<len(intList)):
                                    if(self.couple[j].n.index==intList[l].index):
                                        isRepeat = True
                                        break
                                    l+=1
                                if(isRepeat==False):
                                    intList.append(self.couple[j].n)
                                del self.couple[j]
                                j-=1
                                break
                            if(self.couple[j].n.index==intList[k].index):
                                isSorted = False
                                l = 0
                                while(l<len(intList)):
                                    if(self.couple[j].m.index==intList[l].index):
                                        isRepeat = True
                                        break
                                    l+=1
                                if(isRepeat==False):
                                    intList.append(self.couple[j].m)
                                del self.couple[j]
                                j-=1
                                break
                            k+=1
                        j+=1
                    
                Piese.append(intList)
                i+=1

        i=0
        while(i<len(self.Piese)):
            self.claster.append(Claster())
            j=0
            while(j<len(self.Piese[i])):
                self.claster[i].add(self.Piese[j])
                j+=1
            i+=1
        return self.clasters
    def Analyse():
        numAgregates = len(self.agregates)
        sumWidth = 0
        sumLength = 0
        sumS = 0 
        i = 0
        while(i<len(self.agregates)):
            self.sumWidth+=self.agregates[i].analys()
            self.sumLength+=self.agregates[i].size()
            self.sumS+=self.agregates[i].s_Full()
        self.avgWidth = sumWidth/self.numAgregates
        self.avgS = sumS/self.numAgregates
        self.avgLength = self.Particle.size()/(self.agregates.size()+(self.Particle.size()-sumLength))
        print(avgWidth)
    def getTime():
        return time 
    def getNumPies():
        return numAgregates
    def getAvgWidth():
        return avgWidth
    def getAvgLength():
        return avgLength
    def getAvgS():
        return avgS

