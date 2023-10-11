import math 
A = float(input("Enter the value of A: "))
B = float(input("Enter the value of B: "))
C = float(input("Enteer the vlaue of C: "))
D = B**2-4*A*C
# print(D)
if(D==0):
    x1=-B/(2*A)
    x2=x1
    print("x1=",x1)
    print("x2=",x2)
elif(D>0):
    x1=(-B+math.sqrt(D))/(2*A)
    x2=(-B-math.sqrt(D))/(2*A)
    print("x1=",x1)
    print("x2=",x2)
else:
    print("Roots are imagainary")
print("exited program succesfully")