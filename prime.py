a=int(input("Enter a number"))
if a==1 or a==2:
    print "Prime"
else:
    flag=0
    w=2
    while w<a:
        if a%w==0:
            flag=1
        w+=1
    if flag==0:
        print "Prime"
    else:
        print "Not prime"
