#default mode is read mode
file = open('file.txt', 'r')
print(file.mode)
print(file.readable())
print(file.writable())

#raed data as a list, so we can use for loop to access it
data = file.readlines()
print(data)
'''
#\n make cursor go to next line basically
file.write("Python file create\n")
file.write("Second line\n")
content = ["data1", "data2", "data3"]
#this will write as a list, and each value is 1 line
for each_line in content:
    file.write(each_line + "\n")
'''
file.close()

sfile = 'file.txt'
dfile = 'newfile.txt'

sf = open(sfile, 'r')
content = sf.read()
sf.close()

df = open(dfile, 'w')
df.write(content)
df.close()
print(__name__)