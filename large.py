n=int(input("First No"))
n1=int(input("Second No"))
n2=int(input("Third No"))
if n>n1 and n>n2:
	print("Largest No:"+str(n))
elif n1>n2:
	print("Largest No:"+str(n1))
else:
	print("Largest No:"+str(n2))
