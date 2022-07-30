#unordered collections of UNIQUE elements
myset = set()
myset.add(1)
print(myset)
myset.add('test')
print(myset)

mylist = [1,1,1,1,2,3,3,4,5,1,2]
print(mylist)
mylist.sort()
print(mylist)
#by converting a list to a set we extract all unique elements from list 
newlist = set(mylist)
print(newlist)
