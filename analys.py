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
        return self.s(self.claster[self.getInd(True)],self.claster[self.getInd(False)])
    
    def s(self,a,b):
        d = self.radius(a,b)
        return math.pi * math.pow((d+self.r),2)

    def radius(self,a,b):
        return (math.sqrt(math.pow(math.fabs(a.x-b.x),2)+math.pow(math.fabs(a.y-b.y),2))/2)

    def heigh(self,a,b):
        return math.sqrt(math.pow(math.fabs(a.x-b.x),2)+math.pow(math.fabs(a.z-b.z),2))

    def s_Full():
        return 2*math.pi * radius(self.claster[getInd(True)],self.claster[getInd(False)])*heigh(self.claster[getIndHeigh(True)],self.claster[getIndHeigh(False)])

    def getIndHeigh(self,isPiesA):
        ind1 = 0
        ind2 = 0
        range = 0.0
        i = 0
        while (i<len(self.claster)):
            j = i
            while (j < len(self.claster)):
                if(range < math.sqrt(math.pow(math.fabs(self.claster[i].x-self.claster[j].x),2)+math.pow(math.fabs(self.claster[i].z)-math.fabs(self.claster[j].z),2))):
                    ind1 = i
                    ind2 = j
                    range = math.sqrt(math.pow(math.fabs(self.claster[i].x-self.claster[j].x),2)+math.pow(math.fabs(self.claster[i].z)-math.fabs(self.claster[j].z),2))
                j+=1
            i+=1
        if (isPiesA):
            return ind1
        else:
            return ind2

    def getInd(self,isPiesA):
        ind1 = 0
        ind2 = 0
        range = 0.0
        i = 0
        while (i<len(self.claster)):
            j = i
            while (j < len(self.claster)):
                if(range < math.sqrt(math.pow(math.fabs(self.claster[i].x-self.claster[j].x),2)+math.pow(math.fabs(self.claster[i].y)-math.fabs(self.claster[j].y),2))):
                    ind1 = i
                    ind2 = j
                    range = math.sqrt(math.pow(math.fabs(self.claster[i].x-self.claster[j].x),2)+math.pow(math.fabs(self.claster[i].y)-math.fabs(self.claster[j].y),2))
                j+=1
            i+=1
        if (isPiesA):
            return ind1
        else:
            return ind2

        
    def size():
        return len(self.claster)

class couple_Pies :
    def __init__(self,m_,n_,mx,my,mz,nx,ny,nz):
        self.m = Pies(m_,mx,my,mz)
        self.n = Pies(n_,nx,ny,nz)
class Point:
    range = 3.0
    link = ""
    avgWidth = 0
    numAgregates = 0
    avgLength = 0
    avgS = 0
    time = 0

    def __init__(self,len,es):
        self.couple = []
        self.Particle = []
        self.agregates = []
        k = 0
        while (k < len):
            self.Particle.append(Pies(k,es.part[k].pos[0],es.part[k].pos[1],es.part[k].pos[2]))
            k+=1
        self.couple = self.findCouple()
        self.agregates = self.clasterForm()
        print(self.agregates[0].analys())
    
    def findCouple(self):
        self.arr = []
        i = 0
        while(i<len(self.Particle)-1):
            j = i+1
            while(j<len(self.Particle)):
                if(math.sqrt(math.pow(self.Particle[i].x-self.Particle[j].x,2)+math.pow(self.Particle[i].y-self.Particle[j].y,2)+math.pow(self.Particle[i].z-self.Particle[j].z,2))<=self.range):
                    self.arr.append(couple_Pies(i,j,self.Particle[i].x,self.Particle[i].y,self.Particle[i].z,self.Particle[j].x,self.Particle[j].y,self.Particle[j].z))
                j+=1
            i+=1
        return self.arr

    def clasterForm (self):
        self.claster = []
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
                                isRepeat = False
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
                                isRepeat = False
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
                    
                self.Piese.append(intList)
                print(intList)
                i+=1
        i=0
        while(i<len(self.Piese)):
            self.claster.append(Claster())
            j=0
            while(j<len(self.Piese[i])):
                self.claster[i].add(self.Piese[i][j])
                j+=1
            i+=1
        return self.claster

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

