import analys
import graphData
class part:
    def __init__(self):
        self.pos = []
        print(self.pos)
    def add(self,x,y,z):
        self.pos.append(x)
        self.pos.append(y)
        self.pos.append(z)
        print(self.pos)
class testParam:
    part = []
    def __init__(self):
        print('testParam init')
    def add (self,x,y,z):
        self.part.append(part())
        self.part[-1].add(x,y,z)


test = testParam()
test.add(0,0,0)
test.add(1,1,1)
test.add(2,2,2)

test.add(11,11,11)
test.add(12,12,12)
test.add(13,13,13)
test.add(13,13,14)
print(test.part[0].pos)

pointTest = analys.Point(7,test)
print(pointTest.Analyse().size)

x = [1,2,3,4,5]
y = [2,4,6,8,10]
graph = graphData.Graph()
graph.export(x,y)
print(graph.LagrangeAprox(1.4,graph.dataGraph,4))