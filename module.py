#module is for reusablility
#import data_structure
#import math

#can only import particular module or import everything by *
from math import pi,pow
#simplify the name
import platform as pt
import getpass as gp
import sys
#print(data_structure.my_list)
#print(math.pi)
#print(math.pow(2,3))

#now we can directly use it besides using math.something
print(pi)
print(pow(2,3))
#print(pt.system())
#print(dir(pt))
#print(pt.python_version())
#print(pt.machine())
#print(pt.release())
#print(pt.platform())
#print(pt.architecture())
print(pt.uname())

#while typing something, do not display on the command line
#pw = gp.getpass("enter your password: \n")
#print(pw)
#print(sys.platform)
#print(sys.version_info)
#print(sys.path)
#print(dir(sys))
a = 5 

if(a < 6):
    sys.exit('a is less than 6')
else:
    sys.exit()