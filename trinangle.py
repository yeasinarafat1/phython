import math
a = float(input("enter the value of a: "))
b = float(input("enter the value of b: "))
c = float(input("enter the value of c: "))
if(a+b)>c and (b+c)>a and (c+a)>b:
    s = (a+b+c)/2
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("the ans is :",area)
else:
    print("this is wrong triangle")
    