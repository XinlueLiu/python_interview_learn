#key value pair
my_dict = {'key1':'value1', "key2":'value2'}
print(my_dict['key1'])
my_dict = {'str':'strval', "list":[0,1,2], 'dict':{'dict1':1, 'dict2':2}}
print(my_dict['list'])
print(my_dict['dict']['dict2'])
print(my_dict['str'][0].upper())

#add element to dictionary
my_dict['str2'] = 'is it a string'
print(my_dict)

#update. Can also update an existing method
#in this case, only adding when laptop not in keys
#update is handy when you want to update existing dictionary with another dictionary
#aviod for loop like this
# for key, value in n.items():
#     d[key] = value
if ("laptop" not in my_dict):
    my_dict.update({"laptop":'apple'})
    print(my_dict)

my_dict['laptop'] = 'dell'
print(my_dict)
#delete a specific key-value pair
del my_dict['laptop']
print(my_dict)

#returns keys and values
print(my_dict.keys())
print(my_dict.values())
#returns items as a tuple
print(my_dict.items())

for key,value in my_dict.items():
    print(f'key is {key}, value is {value}')

for key in my_dict.keys():
    print(f'key is {key}')

for value in my_dict.values():
    print(f'value is {value}')