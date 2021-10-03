#// is floor devision. Number will be round towards negative infinity
print(-5//2) #this will be -3
print(5//2) #this will be 2
#find ascii code
print(ord('a'))
#find corresponding character
print(chr(97))
#python will compare character by character
print('abc' < 'aac')
print('abc' < 'z')

a = 5
b = 19
#is/isnot identity operator
print(type(a) is not type(b))

list = [1,2,3]
#membership operator
#in/not in
if a not in list:
    print("not in the list!")
else:
    print("in the list")

print(bool(a) & bool(b))


