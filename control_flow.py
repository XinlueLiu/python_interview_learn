#if
if (1 > 2):
    print("true")
elif (1 == 2):
    print("elif")
else:
    print("false")

#for loop
iterable_val = [1,2,3,4]
for each_item in iterable_val:
    print(each_item)

iterable_tuple = [(1,2), (3,4), ('test', 'ababa')]
for item1,item2 in iterable_tuple:
    print(item1)
    print(item2)

iterable_dict = {'k1':1, 'k2':2, 'k3':3}
#this only print out the keys
for keys in iterable_dict:
    print(keys)
#this prints out the key-value pair
for items in iterable_dict.items():
    print(items)
#can use this to print out key or value
for key,value in iterable_dict.items():
    print(key)
    print(value)
#this only prints out the values
for value in iterable_dict.values():
    print(value)

#while loops
x = 0
while (x < 5):
    print(f'incrementing value of x is {x}')
    x = x + 1
else:
    pass
print(x)
#have break, continue,pass
#pass: does nothing
#break: break out of the loop
#continue: goes to the top of loop