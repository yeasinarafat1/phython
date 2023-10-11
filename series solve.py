def series(a,b,n):
    d = b-a
    N = a+(n-1)*d
    print(f"The {n}th number is : {N}")
def series_sum(a,b,n):
    d = b-a
    s = (n/2)*(2*a+(n-1)*d)
    print(f"The sum of the {n} number of the series is {s}")
x1 = int(input("Enter the value of first number : "))
x2 = int(input("Enter the value of sceond number : "))
x3 = int(input("Enter the value of  n : "))
series(x1,x2,x3)
series_sum(x1,x2,x3)
