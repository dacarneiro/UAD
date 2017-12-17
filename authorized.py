import csv
import numpy as np


with open('final.csv', 'r') as f:
    #reader = csv.reader(f)
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    all_plugins_list = list(reader)

#print(all_plugins_list[2][0])



with open('UADSystemProfile.txt' , 'r') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    array_my_plugins_temp = list(reader)


counter = len(array_my_plugins_temp)
save = 0

i = 0
array_my_plugins = []
while i < counter:
    #print(array_my_plugins_temp[i])
    if "\t\t\t UAD-2 Plug-in Authorizations \t\t\t" in array_my_plugins_temp[i]:
        save = 1
    if save == 1:
        array_my_plugins.append(array_my_plugins_temp[i])
    i = i + 1

#print(array_my_plugins[2][1])
#print(len(array_my_plugins))

array_matched_plugins = []
counter_my = len(array_my_plugins)
counter_all = len(all_plugins_list)
i = 2
j=0
while i < counter_my:
    j = 0
    while j < counter_all:
        #print(array_my_plugins[i])
        #print(all_plugins_list[j][0])
        if (array_my_plugins[i][0] == all_plugins_list[j][0] and array_my_plugins[i][1] != " Demo not started"):
            array_matched_plugins.append(all_plugins_list[j])
        j = j + 1
    i = i + 1

print(array_matched_plugins)
print(len(array_matched_plugins))