n = int(input("enter the maximum value: "))
for a in range(1,n+1):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(c_square)**0.5
        if (c_square-c**2) == 0:
            print(a,b,c)
