import csv
filename = raw_input("Please enter the csv file you'd like to use (i.e. names.csv)>>")
names = []
while filename != "END":
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] not in names:
                names.append(row[0])
    filename = raw_input("Please enter the csv file you'd like to use (i.e. names.csv)>>")    

with open('final.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for name in names:
        spamwriter.writerow([name])
