# a callback function is a function that is passed as an argument to the other function
# this other function is expected to call this callback function in its definition
# generally used with asynchronous functions

def CallbackFunc(s):
    print("length of the text file is : ", s)

def PrintFileLength(path, callback):
    f = open(path, 'r')
    length = len(f.read())
    f.close()
    callback(length)

if __name__ == '__main__':
    # dont do CallbackFunc() because we are just passing function
    # not calling it now
    PrintFileLength("testfile.txt",CallbackFunc)
