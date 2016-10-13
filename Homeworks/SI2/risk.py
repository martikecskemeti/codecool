from random import randint

while True:
    a_unit = input("How many units attack?")
    if a_unit.isdigit():
    	a_unit = int(a_unit)
    	if a_unit < 4 and a_unit > 0:
    		break

while True:
    d_unit = input("How many units defend?")
    if d_unit.isdigit():
    	d_unit = int(d_unit)
    	if d_unit < 3 and d_unit > 0:
        	break

Attacker = []
Defender = []


for i in range(int(a_unit)):
	Attacker.append(randint(1,6))
	

for i in range(int(d_unit)):
	Defender.append(randint(1,6))
	
	
	
Attacker.sort()
Defender.sort()

Attacker = Attacker[::-1]
Defender = Defender[::-1]



print ("")
print ("Dice:")	
print (" " *2 + "Attacker: " + str(Attacker)[1:-1].replace(", ", "-"))
print (" " *2 + "Defender: " + str(Defender)[1:-1].replace(", ", "-"))


a = 0
d = 0

for i in range(0,2):
	if Attacker[i] > Defender[i]:
		a += 0
		d += 1
	else:
		a += 1
		d += 0
		
print ("")		
print ("Outcome:")
print ("  Attacker: Lost %d units" % a)
print ("  Defender: Lost %d units" % d)



