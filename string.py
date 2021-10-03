#a string is a sequence of characters
#in python, string is a sequence of unicode character
#access character in a string
my_name = "luelue luelue"
#0:3 will get 3 characters, not 4
print(my_name[0:3])
#length of string
print(len(my_name))
#concatinate two string
course = "python"
word = my_name + " is taking course " + course
print(word)

#dot does not modify the original string
print(my_name.lower())
print(my_name.upper())
#lower case to upper case, upper case to lower case
print(my_name.swapcase())
#starting letter of each word capitalize
print(my_name.title())
#only the starting letter will be capitalize
print(my_name.capitalize())
#good for unicode
print(my_name.casefold)
#dir prints out the available operations on the string
print(dir(my_name))

print("*********************")
#is it starts with letter l?
#also have endswith
print(my_name.startswith("L"))
print(my_name.startswith("luelue"))
#also have isupper
print(my_name.islower())
#is starting character of each word captalized
print(my_name.istitle())
#is the string only contains space
print(my_name.isspace())

print("*********************")
#-, *d, \n
join_name = "-".join(my_name)
name = "chongchongchong!"
print(join_name)
print(join_name.center(50))
print(name.center(50))
#fill up the extra space with 0
print(name.zfill(20))
x = " python3 is python"
#strip remove space starting left or right
print(x.strip())
#remove the one on right
print(x.rstrip('python python'))
#replace p with d
print(x.replace("p", "d"))
#we can have multiple strip like x.strip('p').strip('t')

print(x.split('is'))

print("*********************")
print(x.count('p'))
print(x.count('python'))
#if find is not found, return -1. if index is not found, raise exception
print(x.find('p'))