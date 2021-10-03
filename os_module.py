import os
import platform
print(os.getcwd())
print(os.listdir())
#create a path
os.mkdir('test')
os.makedirs('udemy/learn')
os.removedirs('udemy/learn')
os.rmdir('test')
#os.rename(src,dst)
print(os.getuid())
print(os.getpid())

print(os.path.sep)
path = "/Volumes/Macintosh HD - Data/Users/xinlueliu/saved_files/python/os_module.py"
print(os.path.basename(path))
print(os.path.dirname(path))
#can use os.path.join(path1,path2) to combine two paths. 
#Else use string addition and path seperator

#this will return a tuple with dirname and basname
print(os.path.split(path))

#check whether path is there(if condition)
if os.path.exists(path): 
    print("file is present")
else:
    print("file doesn't exist")

if os.path.isfile(path): 
    print("given path is a file")
else:
    print("given path is NOT a file") 

if os.path.isdir(path): 
    print("given path is a directory")
else:
    print("given path is NOT a directory") 

print(os.getcwd())
#be able to exexute system command in python
#return 0 if success. Nonzero if failed
path_success = os.system("pwd")
if (~path_success) :
    print("command excuted successfully")
else:
    print("command failed")

print(platform.system())

walk_path = "/Volumes/Macintosh HD - Data/Users/xinlueliu/saved_files/python"
#give a list of a tuple with 3 elements of lists
#first element is the given path, 2nd element is the directory in this path
#third element is the files in this path

#if we have a directory, then the directory will be added to new path
#and python will search that directory as well, and create another tuple
print(list(os.walk(walk_path)))
print("*******************************")
#we can unpack tuple in this way
#can use topdown = False to print from bottom up
for root, directory, file in os.walk(walk_path):
    #if there is at least 1 file
    if(len(file)):
        print(root,directory,file)
        for each_file in file:
            #print(each_file)
            #print complete path
            print(os.path.join(root, each_file))

for each in os.walk(walk_path):
    print(each)