def f1(raw):
    if raw==4:
        return 1
    else:
        def f2(col):
            if col == 4:
                return 1
            else:
                if (raw==0 and col%4!=0) or (raw==1 and raw +col==1) or (raw==2 and raw+col==2) or (raw==3 and col%4!=0):
                    print("♥️",end=" ")
                    f2(col+1)
                else:
                    print(end=" ")
                    f2(col+1)
        f2(0)
    print( )
    f1(raw+1)
f1(0)