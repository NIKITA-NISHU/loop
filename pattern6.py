i=2
while i<=30:
    j=1
    while j<=i:
        if j%i==0:
            print(i,end=" ")
        j+=1
    print()
    i+=2