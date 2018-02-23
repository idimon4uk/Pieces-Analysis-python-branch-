import analys
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
print(test.part[0].pos)

pointTest = analys.Point(2,test)
