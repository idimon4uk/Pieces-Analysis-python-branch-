import math


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Graph:
    def __init__(self):
        self.dataGraph = []

    def export(self, x, y):
        if(len(x) != len(y)):
            print("Uncorrect data (len of x != len of y")
            return
        else:
            i = 0
            while (i < len(x)):
                self.dataGraph.append(Point(0, 0))
                self.dataGraph[-1].x = x[i]
                self.dataGraph[-1].y = y[i]
                i += 1

    def nearest_point(self, X0, dataGraph0, n, isNext):
        absDifference = []
        mostabsDiffSumm = 1
        i1 = 0  # 1st point for aprox || isNext = true
        i2 = 3  # 2nd point for aprox || isNext = false
        i = 0
        while(i < n):
            absDifference.append(0)
            absDifference[-1] = math.fabs(dataGraph0[i].x - X0)
            i += 1
        mostabsDiffSumm = absDifference[0] + absDifference[1] + absDifference[2] + absDifference[3]
        i = 3
        while (i < n):
            if ((absDifference[i] + absDifference[i - 1] + absDifference[i - 2] + absDifference[i - 3]) < mostabsDiffSumm):
                mostabsDiffSumm = absDifference[i] + absDifference[i - 1] + absDifference[i - 2] + absDifference[i - 3]
                i1 = i-3
                i2 = i
            i += 1
            if (isNext):
                return i1
            else:
                return i2

    def LagrangeAprox(self, X0, dataGraph0, n):
        i1 = self.nearest_point(X0, dataGraph0, n, True)
        i2 = self.nearest_point(X0, dataGraph0, n, False)
        result = 0
        i = i1
        while(i < i2):
            num = 1
            denum = 1
            j = 0
            while(j < i2):
                if(i != j):
                    denum *= dataGraph0[i].x - dataGraph0[j].x
                    num *= X0-dataGraph0[j].y
                j += 1
            result += dataGraph0[i].y*(num/denum)
            i += 1
        return result
