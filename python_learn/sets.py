# unordered collections of UNIQUE elements
# mutable. we can add/remove item, but cannot change item assignment
myset = set()
myset.add(1)
print(myset)
myset.add('test')
print(myset)
myset.remove(1)
print(myset)

mylist = [1,1,1,1,2,3,3,4,5,1,2]
print(mylist)
mylist.sort()
print(mylist)
#by converting a list to a set we extract all unique elements from list 
newlist = set(mylist)
print(newlist)
