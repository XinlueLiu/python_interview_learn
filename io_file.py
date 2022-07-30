with open('testfile.txt','r+') as myfile:
    lines = 'testtteestest\nnewline'
    myfile.write(lines)
    #move the cursor to the beginning of the file
    myfile.seek(0)
    print(myfile.read())
    myfile.seek(0)
    #get each line as an object in a list
    print(myfile.readlines())
    #by using with open, file is automatically close. 
    #Otherwise need to manually close the file