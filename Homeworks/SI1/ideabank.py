import sys

ideabank = open("ideabank.txt", "a+")

if "--list" in sys.argv:
    
    ideabank = open("ideabank.txt", "r")

    x = 0
 
    print ("Your ideabank: ")

    for line in ideabank:
        x += 1
        print (str(x) + ". " + line, end="")

elif "--delete" in sys.argv:
    
    ideabank = open("ideabank.txt", "r+")

    x = 0
    z = 0

    y = int(sys.argv[2])
    rows=[]
   
    for line in ideabank:
        x += 1
        line = str(x) + line + ""
        rows.append(line)

    ideabank.seek(0)

    print ("Your ideabank: ")

    for n in rows:
        if n[0] != str(y):
            n = n[1:]
            z += 1
            print (str(z) + ". " + str(n), end="")
            ideabank.writelines(n)

    ideabank.truncate()
            
else:
    
    ideabank = open("ideabank.txt", "r+")

    x = 0
           
    new = input("What is your new idea:")

    ideabank.writelines(new)
    ideabank.writelines("\n")

    print ("\n" + "Your ideabank: ")

    for line in ideabank:
        x += 1
        print (str(x) + ". " + line, end="")

    print (str(x + 1) + ". " + new)
    
            
ideabank.close()




