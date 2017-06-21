a=int(input("Enter a Number"))
first=a
rev=0
while a!=0:
    re=a%10
    rev=rev*10+re
    a=a/10
if first==rev:
    print "Palindrome"
else:
    print "Not a Palindrome"
