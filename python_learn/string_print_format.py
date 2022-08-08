#python has variable data types, and can use type() to display the type of the data type
test = 1
print(f'type of variable test is {type(test)}')
test = "dog"
print(type(test))
print(test)

#Strings
# ordered sequences, so can use indexing or slicing to grab sub-sections of string
test = "testing the index"
print(test[0])
# get the last item
print(test[-1])
#from test[2](s) all the way to end
#up to is [:n], but NOT including n
print(test[2:])
#secitons of the string [start:stop:step]
#this will INCLUDE start position, but NOT INCLUDE stop
print(test[0:6:2])
#[::] means all the way from start to finish, 2 means jump size of 2. INCLUDING leading t
print(test[::2])
#reserve the string.
print(test[::-1])

#Strings are immutable. cannot do test[0] = 'P'
#string concatenation
print('play ' + test)
#pring 10 zs
print('z' * 10)
#count, find, center, 


#build_in methods
#capitalize first character
print(test.capitalize())
# upper case all characters
print(test.upper())
#default split based on white space. split into a list!
print(test.split())
#split based on characters. e is removed!
print(test.split('e'))

#print formatting
print('string formating {}'.format('TESTING'))
#print based on index position
print('String index formating {1} {2} {0}'.format('aaa','bbb','ccc'))
print('String index formating {p1} {p2} {p0}'.format(p0='aaa',p1='bbb',p2='ccc'))

result = 100/666
print(result)
#floating format {value:width.precision f}. width is total width of string number. Will add leading white spaces
print('result = {val:10.2f}'.format(val=result))

#or use the f format
print(f'fvalue is {result:10.2f}')


#hex
print(hex(124))
#binary
print(bin(234))
#2**5 % 4
print(pow(2,5,4))
#round
print(round(3.49))
#round to 2 decimals
print(round(3.1415926,3))