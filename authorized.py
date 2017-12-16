import csv
import numpy as np
#fname = open('UADSystemProfile.txt','r')
#message = f.read()
#print(message)
#f.close()
save = 0
count = -1
with open("UADSystemProfile.txt", "r") as ins:
    array = []
    for line in ins:

        if "Authorizations" in line:
            save = 1
        if save !=0 and line != "\n":
            count = count+1
            array.append(line)

#print(array[143])
#print(count)

#array_match = []
#f = open('final.csv', 'r')
#reader = csv.reader(f)
#for row in reader:
#    print
#    array_match.append(row)
#f.close()
#print(array_match[2])

x=np.genfromtxt('final.csv',delimiter=';',dtype=None)

Counts = x[:,2]
print(x)

