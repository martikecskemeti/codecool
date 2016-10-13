fibi_numbers = input("how many numbers?")

fibi=[0,1]


for n in range(0,int(fibi_numbers) - 2):
	n = fibi[len(fibi)-2] + fibi[len(fibi)-1]
	fibi.append(n)
	
x =0
for n in fibi:
	x += 1
	print (str(x) + "." + " " * (25 - len(str(x)) - len(str(n))) + str(n))

