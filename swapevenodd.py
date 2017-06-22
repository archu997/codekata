s1=str(raw_input("Enter a string"))
i=0
s=list(s1)
while i<len(s):
    if i+1<len(s):
        s[i],s[i+1]=s[i+1],s[i]

    i+=2

print "".join(s)
