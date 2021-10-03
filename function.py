import file
#this is how to define default argument
def mycode(cmd1 = "default", cmd2 = "default"):
    print(cmd1 + " " + cmd2)
    print(x)
    cmd1 = cmd1 + " what"
    print(f'cmd1 is {cmd1} for mycode')
    return cmd1, cmd2 + " test"

#variable length argument
def display(*data):
    for item in data:
        print(f'hellp {item}')

def keyword_based_arg(**karg):
    for values in karg.values():
        print(f'each value pair is {values}')

def main():
    #global x
    #x = 10
    keyword_based_arg(a = 1, b = "test")
    keyword_based_arg(a = 1, b = "test", c = ["get", "that", "list"])
    '''
    display()
    display("a")
    display(2)
    display(1,2,3,4,"test")
    '''
    '''
    cmd1 = 'hello'
    cmd2 = 'this is a function'
    result1, result2 = mycode(cmd1, cmd2)
    #pass by value
    print(f'cmd1 is {cmd1} for main')
    print(f'result1 is {result1}')
    print(f'result2 is {result2}')
    mycode(cmd2 = "2 by key", cmd1 = "1 by key")
    '''

#if any variable is declared outside of the function, it is a global variable
x = 10
if (__name__ == "__main__"):
    main()
# __name__. If run from code directly, variable will be main
# if run indirectly(say we import a file), __name__ will be the name of the file
#print(__name__)
