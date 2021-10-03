import datetime as dt
import os
import sys
import datetime
print("Hello World")
'''
in python, no curly braces for a block of code
indentation is used to represent a block of code

if 3 > 1:
    print("block of")
    print("test")
    print("what\nis\nnewline\n")
    #\b backspace
    print("t \best")
    print("t\b\best")
    #\t tab
    print("\ttab")
    #\ escape symbol
    print("\"python\"'s test")
    print("/home/this/is/the/path")
    print("C:\\Windows\\path\\this\\is")
'''
#range() used to generate integer
#range(start, stop, step). By default, start = 0 and step = 1
print(list(range(5)))
print(list(range(0,10,2)))


list = [1,4,6,4,'what']

for each in range(len(list)):
    print(f'index --> {each}, value --> {list[each]}')

if True:
    pass

for item in list:
    if(item == 4):
        continue
    print(item)


print(dt.datetime.now())
print(dt.datetime.now().day)
#provide seconds, counts from 1969-12-31 19:00
print(dt.datetime.fromtimestamp(0))
print(dt.datetime.fromtimestamp(999999999))

#format time result into a string
save_time = dt.datetime.now().strftime("Year: %Y, Month: %m, Date: %d")
print(save_time)

req_path=input("Enter your path: ")
age=0
if not os.path.exists(req_path):
   print("Please provide valid path ")
   sys.exit(1)
if os.path.isfile(req_path):
   print("Please provide directory path ")
   sys.exit(2)
today=datetime.datetime.now()
for each_file in os.listdir(req_path):
   each_file_path=os.path.join(req_path,each_file)
   if os.path.isfile(each_file_path):
      file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
      #print(dir(today-file_cre_date))
      dif_days=(today-file_cre_date).days
      if dif_days > age:
         print(each_file_path,dif_days)
