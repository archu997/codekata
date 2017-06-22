n1=int(input("First Interval"))
n2=int(input("Second Interval"))
for a in range(n1,n2+1):
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
