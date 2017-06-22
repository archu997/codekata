b2=int(input("Enter a range"))
for a in range(2,b2+1):
    if a==2:
        print a
    else:
        flag=0
        w=2
        while w<a:
            if a%w==0:
                flag=1
            w+=1
        if flag==0:
            print a
