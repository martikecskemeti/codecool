from random import randint

def get_unit(text, high, low):
    while True:
        n = input("How many units " + text + "? ")
        if n.isdigit():
            n = int(n)
            if n < high and n > low:
                return n

Attacker = []
Defender = []


for i in range(int(get_unit("attack", 4, 0))):
	Attacker.append(randint(1,6))
	

for i in range(int(get_unit("defend", 3, 0))):
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

for i in range(0,min(len(Attacker),len(Defender))):
	if Attacker[i] > Defender[i]:
		d += 1
	else:
		a += 1
	
print ("")		
print ("Outcome:")
print ("  Attacker: Lost %d units" % a)
print ("  Defender: Lost %d units" % d)
