def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
x = int(input("How many fibbonnci number do you want? : "))
b=0
for i in range(x):
    b = b+1
    print(fibonacci(b))