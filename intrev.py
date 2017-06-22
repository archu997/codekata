a=int(input("Enter a number"))
rev=0
while a!=0:
    re=a%10
    rev=rev*10+re
    a=a/10
print rev
