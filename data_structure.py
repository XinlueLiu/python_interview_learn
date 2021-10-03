#four build-in data structures
#list[], tuple(), dictionary,{} set{}

#list is mutable, string and tuple are not mutable
my_list = [1,2,'what', 'this is a list',2]
#can access 'h' from 'this is a list'
print(my_list[3][1], type(my_list))
#print from index 1(2) to the last element
print(my_list[1:])
my_list[0] = 1234
print(my_list)
#print the index of 2. 2,2 means index for 2nd 2
print(my_list.index(2,2))
#clear the list
#my_list.clear()
#print(my_list)

#directly assign. both points to the same memory location. 
#so one changes, the other one also changes
my_new_list = my_list
#create another list with another memory location
my_new_copy_list = my_list.copy()
my_new_list[0] = 3
print(my_new_list)
print(my_list)
#so this won't get changed
print(my_new_copy_list)

print(id(my_list))
print(id(my_new_list)) #same id location
print(id(my_new_copy_list)) #different id location

#add at the end
my_list.append('append')
print(my_list)
#insert can insert at specific position
my_list.insert(1, "insert here")
print(my_list)

#add as a list(to the last element)
my_list.append(my_new_copy_list)
print(my_list)
#add as normal. 
my_list.extend(my_new_copy_list)
print(my_list)

#pop can remove element
#by default it will remove last element


#Tuples are inmutable
my_tuple = (3,4,[4,5,6],'test',5)
print(my_tuple)
print(my_tuple, type(my_tuple), len(my_tuple))

#dictionary has keys and their values
my_dict = {'fruit':'apple', 'school':'cmu', 3:'three'}
print(my_dict)
#if we dont have a key, this one will throw an exception
print(my_dict['school'])
#if we dont have a key, .get() will return None 
print(my_dict.get('school'))
#if assigning the same key, value will be updated
my_dict['undergrad'] = 'Purdue'
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
#getting each key value pair as an item
print(my_dict.items())

#if we want to add one dictionary to another dictionary, use update
my_dict.pop('fruit')
print(my_dict)
#removes and returns the last element pair inserted into the dictionary
removed_item = my_dict.popitem()
print(removed_item)

#fromkeys can be used to create a dictionary from keys(with empty values)
#we can then assign values later
keys = [1,2,3,4,5]
dict_keys = dict.fromkeys(keys)
print(dict_keys)
dict_keys[1] = '1'
print(dict_keys)

#if key is there, it won't modify the value. If key is not there, we will add the 'default' value
#setdefault

#in python3, dictionary is ordered

#set
my_set = {5,1,6,6}
a = {1,2,'what'}
#will be ordered and duplicates will be removed automatically
print(my_set)
print(a.union(my_set))
print(a.intersection(my_set))