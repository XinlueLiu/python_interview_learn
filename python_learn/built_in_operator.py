# range up to. in this case not including 10, but including 0, the start val
# (start,step,step)
for num in range(0,10,2):
    print(num)

# can type cast
print(list(range(0,10,2)))

# enum
# typical
index_cnt = 0
word = 'abcde'
for letter in word:
    print(word[index_cnt])
    print(letter)
    index_cnt += 1

# get back a tuple
for item in enumerate(word):
    print(item)

for index,letter in enumerate(word):
    print(f'index is {index}, letter is {letter}')

# zip, also returns a tuple. only zip matching length. In this case, 3 items
list1 = [1,2,3,4]
list2 = ['a','b','c']
for item in zip(list1, list2):
    print(item)

print(list(zip(list1,list2)))

# in 
if 'x' in list1:
    print('in the list')
else:
    print('NOT IN THE LIST!')

my_dict = {'key1':'value1', "key2":'value2'}
if 'value1' in my_dict.values():
    print('in the dict value')
else:
    print('NOT IN THE DICT VALUE!')

if 'value1' in my_dict.keys():
    print('in the dict keys')
else:
    print('NOT IN THE DICT KEYS!')

# random
from random import shuffle
mylist_random = [1,2,3,4,5,6,7,8,9,0]
# randomly shuffle the list. IN-PLACE function
shuffle(mylist_random)
print(mylist_random)

from random import randint
# (lower_bound, upper_bound)
print(randint(0,100))

# input function to accept user input
# this will always accept as a STRING!
result = input('Enter a number here\n')
if int(result) == 5:
    print("int 5!")
elif result == '5':
    print(f'result is string {result}')
else:
    print("not five")

#list apprehension
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)
print(mystring)
