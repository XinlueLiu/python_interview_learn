#ordered sequences that can hold variety of object types
my_list = [1,2,3]
print(my_list)
my_list = [1,2,'test']
print(my_list)
#len prints the length of the list
print(len(my_list))
#slicing and concatenating
print(my_list[0])
new_list = ['new_list', 'aaa']
print(my_list + new_list)

#can mutate and change the list
new_list[0] = new_list[0].upper()
print(my_list + new_list)
#append append the end, pop pop from the end. Can also pass index position for pop
new_list.append('append new object')
print(my_list + new_list)
popItem = new_list.pop()
print(my_list + new_list)
print(popItem)

num_list = [1,2,7,5,3,4,77]
print(num_list)
#sort occur IN PLACE, does not return anything. return NoneType
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)