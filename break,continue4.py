i=1
sum=0
while i<=11:
    weight=int(input("enter the weight="))
    sum=sum+i
    average=sum/11
    i+=5
    if weight%5==0:
        continue
    print(i)

