n=int(input("Enter a number"))
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+r**3
    n=n/10
if temp==sum:
    print "armstrong number"
else:
    print "Not an armstrong number"
