def say_hello():
    print("hello")

say_hello()


def hello_name(name = 'Default'):
    print(f'hello {name}')

hello_name('Ed')
hello_name()

def add_num(num1, num2):
    return num1+num2

sum_num = add_num(1,2)
print(sum_num)


#*args & **kwargs
#btw sum only takes iterable operands
def myfunc(a,b):
    return sum((a,b)) * 0.05

print(myfunc(4,5))

#can use *args will takes in arbitrary numbers of arguments
#this args will be treated as a tuple
def myfunc(*args):
    print(args)
    return sum(args) * 0.05

print(myfunc(4,5,5,6,7,8,2345,234524,132))

#**kwargs builds a dictionary or key-value pairs
def myfunc(**kwargs):
    #treat fruit as a key
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('not fruit!')

myfunc(test='apple')
myfunc(fruit='apple', test='apple')

#map function
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
#map function to each item of the list
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))
print(list(map(str, my_nums)))

#filter will fiter out based on function condition(key values that match filter condition)
def check_even(num):
    return num%2 == 0

for n in filter(check_even, my_nums):
    print(n)

print(list(filter(check_even, my_nums)))

#can use lamda function is only intended to use function once