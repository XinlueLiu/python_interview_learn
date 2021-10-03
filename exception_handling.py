def main():
    try:
        print(4 / 0)
    #run this code if an exception occurs
    #if exception is know, we can except known_name and deal with it
    except Exception as err:
        print(f'we are having error: {err}')
    else:
        print("this will only execute when no exceptions")
    finally:
        #code in finally will always be executed
        print("always attention")

def readfile():
    try:
        fo = open("lue.txt")
        print(fo.readlines())
        fo.close()
    except Exception as err:
        print(f'we are having error: {err}')


if (__name__ == "__main__"):
    main()
    readfile()
    #manually raise exception
    #raise Exception("this is an exception")
    age = int(input("input your age\n"))
    if (age > 140):
        raise Exception("this is not a valid age")
    else:
        print(f'age is {age}')
    #raise assertion error if condition is false
    assert 3 > 4