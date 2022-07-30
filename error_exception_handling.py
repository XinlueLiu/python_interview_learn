#try, except, finally
#try: code to be attempted
#except: code will excute if an error in try block is encountered
#finally: final block of code to be executed. regardless of errors

from typing import Type


try:
    f = open('testfile','r')
    f.write("write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("OS error")
except:
    print("all other errors!")
finally:
    print("I always run")
print("continue with program")

#decorator
#change the behaviour of a function or class but without permanetly modifying it
#can switch it on or off