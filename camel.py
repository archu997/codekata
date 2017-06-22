s=raw_input("Enter a string with space")
def camel(s):
    w=s.split(" ")
    return w[0]+''.join(i.title() for i in w[1:])
print camel(s)
