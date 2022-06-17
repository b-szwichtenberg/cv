
from fractions import Fraction
import random
class color:
    RED = '\033[91m'
    RESET = '\033[0m'

def function(x):
    F=(x+Fraction(1))/x
    return F


def insert(x, b0, b1, b2, b3, nodex):
    result = b0 + b1 * (x - nodex[0]) + b2 * (x - nodex[0]) * (x - nodex[1]) + b3 * (x - nodex[0]) * (x - nodex[1]) * (x - nodex[2])
    return result

def error(node_function, after_insert):
    result = 0
    for i in range(0, 151):
        subtract = node_function[i] - after_insert[i]
        if subtract < 0:
            subtract *= -1
        if subtract > result:
            result = subtract
    return result
    
def display(list,n):
    for i in range(0, n):
        print(list[i], end=' ')

node=[Fraction(1,3),Fraction(2,5),Fraction(1,2),Fraction(3,5),Fraction(2,3),Fraction(3,4),Fraction(4,5),Fraction(1),Fraction(6,5),Fraction(5,4),Fraction(4,3),Fraction(7,5),Fraction(3,2),Fraction(8,5),Fraction(5,3),Fraction(7,4),Fraction(9,5),Fraction(2)]
variable=True

while(variable):
    n=0
    print(color.RED + "x_i:" +color.RESET,end='  ')
    for i in node:
        print(color.RED + str(n) + color.RESET,end='')
        print(":",end='')
        print(i,end='  ')   
        n=n+1
    print()
    x0,x1,x2,x3 = input("Wybierz cztery węzły, wpisując wartości z zakresu od 0 do 17 oddzielone spacjami: ").split()
    if(x1.isnumeric() and x0.isnumeric and x2.isnumeric() and x3.isnumeric()):  
        if(int(x0)>-1 and int(x1)>-1 and int(x2)>-1 and int(x3)>-1 and int(x0)<18 and int(x1)<18 and int(x2)<18 and int(x3)<18):
            variable=False
            x0,x1,x2,x3=int(x0),int(x1),int(x2),int(x3)
        else:
            print("Podane wartości były poza zakresem! ")    
    else:
        print("Podane wartości były literami! ")

print()
nodex=[node[x0],node[x1],node[x2],node[x3]]
print("Wartości wybranych węzłów:")
display(nodex,4)
print()

nodey=[function(nodex[0]),function(nodex[1]),function(nodex[2]),function(nodex[3])]
print("Wartości funkcji dla wybranych węzłów:")
display(nodey,4)
print()

b0=nodey[0]
b1=(nodey[1]-nodey[0])/(nodex[1]-nodex[0])
b2=(-nodey[0]-b1*(nodex[2]-nodex[0])+nodey[2])/((nodex[2]-nodex[0])*(nodex[2]-nodex[1]))
b3=(-nodey[0]+nodey[3]-b1*(nodex[3]-nodex[0])-b2*((nodex[3]-nodex[0])*(nodex[3]-nodex[1])))/((nodex[3]-nodex[0])*(nodex[3]-nodex[1])*(nodex[3]-nodex[2]))


print("Wielomian wygląda następująco:")
print("P(x)=",b0,"+",b1,"( x -",nodex[0],") +",b2,"( x -",nodex[0],")( x -",nodex[1],") +",b3,"( x -",nodex[0],")( x -",nodex[1],")( x -",nodex[2],")\n")

node151 = []
for i in range(30, 181):
    node151.append(Fraction(i,90))

node151_function=[]
for i in range(0, 151):
    node151_function.append(function(node151[i]))

after_insert = []
for i in range(0, 151):
    after_insert.append(insert(node151[i], b0, b1, b2, b3, nodex))

print()
print("Największy błąd bezwzględny: ", end=' ')
print(error(node151_function, after_insert))
