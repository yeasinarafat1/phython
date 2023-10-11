import math
# a = int(input("enter the value of a: "))
# b = int(input("enter the value of b: "))
# c = int(input("enter the value of c: "))
def equation(a,b,c):
    D= (b**2)-(4*a*c)
    if(D==0):
        x1=(-b)/(2*a)
        x2=x1
        print("x1=",x1)
        print("x2=",x2)
    elif(D>0):
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print("x1=",x1)
        print("x2=",x2)
    else:
        print("root are imagianary")
equation(4,-9,-5)
equation(1,5,6)
