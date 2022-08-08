n=int(input("enter the rows"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(" ",end='')
        j-=1
    a=i
    while a>=1:
        print("*",end=" ")
        a-=1
    i+=1
    print()
b=n-1
while b>=1:
    print(" "*(n-b),end=" ")
    k=1
    while k<=b:
        print("*",end=" ")
        k=k+1
    b-=1
    print()
    