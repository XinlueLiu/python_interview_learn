#in python, no need to declare variables before using them
#that's why called dynamically typed language
a = 10
print("a")
print(a)
print(type(a))
b = 9.12341
print(b)
print(type(b))
#id will print out the memory location of a
id_a = id(a)
print(id_a)

my_name = "luelue"
print(bool(my_name))
print(my_name)
my_value = True & False
print(my_value)

x = 56
print(x,type(x))
y = str(x)
print(y,type(y))
z = bool(x)
print(z,type(z))
zz = complex(x)
print(zz,type(zz))
print(x,y,my_name)
print("{}, \n{}, {}".format(x,y,my_name))
print(f"{x}, \n{y}, z is {z}")


#delete a variable to free memory
del a
del b
