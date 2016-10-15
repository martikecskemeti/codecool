import sys

# version 1:

def hello(x):
    if len(x)-1 == 1:
         print ("Hello %s!" % x[1])
    else:
        print ("Hello World!")

hello(sys.argv)


"""" 
version 2:
although I'm submitting the first version,
beacuse it was expected to use functions, but
I came up with an other easier solution:

import sys

try:
    print ("Hello %s!" % sys.argv[1])
except IndexError:
    print ("Hello World!")

"""
