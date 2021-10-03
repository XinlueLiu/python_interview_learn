import csv
file = open('testcsv.csv', 'r')
new_csv_file = 'newcsv.csv'
file_new = open(new_csv_file, 'w')
#get data as list
#if seperated as other things, like a |. use delimiter
data = csv.reader(file, delimiter = ",")
csv_write = csv.writer(file_new)
for each in data:
    print(each)
    csv_write.writerow(each)

file.close()
file_new.close()
