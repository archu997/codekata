
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
def convert(rom):
    res=0
    i=0
    while i<len(rom):
        val1=value(rom[i])
        if i+1 <len(rom):
            val2=value(rom[i+1])
            if val1>=val2:
                res=res+val1
                i=i+1
            else:
                res=res+val2-val1
                i=i+2
        else:
            res=res+val1
            i=i+1

    return res
a="MCM"
a=a.upper()
print convert(a)
