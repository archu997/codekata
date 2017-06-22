a1=int(input("First interval"))
a2=int(input("Second interval"))
for n in range(a1,a2+1):
    temp=n
    sum=0
    while n>0:
        r=n%10
        sum=sum+r**3
        n=n/10
    if temp==sum:
        print temp
