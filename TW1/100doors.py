door_num = []

def doors(num):
    for i in range(num):
        door_num.append("X")

doors(100)

a = "X"
b = "O"

def steps(s):
    for y in range(s,len(door_num)+1):
        for x in range(y,len(door_num)+1,y):
            if door_num[x-1] == a:
                door_num[x-1] = b
            else:
                door_num[x-1] = a

steps(1)

result_doors = []

def result(z):
    doors_enum = list(enumerate(door_num, start=1))
    for n in doors_enum:
        if n[1] == z:
            result_doors.append(n[0])

result(b)

print ("The following doors are open: " + str(result_doors)[1:-1])



            

