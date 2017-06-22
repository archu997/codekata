a1=int(input("First interval"))
a2=int(input("Second interval"))
for n1 in range(a1,a2+1):
    l=len(str(n1))
    n=int(n1)
    temp=n
    sum=0
    while n>0:
        r=n%10
        sum=sum+r**l
        n=n/10
    if temp==sum:
        print temp

