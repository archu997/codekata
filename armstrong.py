n1=raw_input("Enter a number")
l=len(n1)
n=int(n1)
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+r**l
    n=n/10
if temp==sum:
    print "armstrong number"
else:
    print "Not an armstrong number"
