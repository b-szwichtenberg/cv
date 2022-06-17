class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __sub__(self,other): #bok kwadratu
        length = self.x - other.x
        return abs(length)

    def __and__(self,other):
        leng = max (self.x,other.x)
        return leng
        
    def __or__(self,other):
        th = min (self.x,other.x)
        return th

#pole kwadratu
def area(length):
    return length*length

#kwadrat A
p1 = Point(1, -1)
p2 = Point(4, 2)
#kwadrat B
p3 = Point(3,-2)
p4 = Point(5,0)

a = p1-p2 #bok kwadratu A
b = p3-p4 #bok kwadratu B
c = area(a)
d = area(b)

e = p1 & p3 #prawy koniec boku wspólnego pola
f = p2 | p4 #lewy koniec
g = (e-f)*(e-f)
print(g,c+d-g)
