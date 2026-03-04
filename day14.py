'''file = open('sample.txt','r')
content = file.read()
print(content)


file = open('sample.txt','r')
content = file.readline()
print(content)


file = open('sample.txt','r')
content = file.readlines()
print(content)'''

'''
file = open('sample.txt','r')

content1 = file.read()
file.seek(0)
content2 = file.readline()
file.seek(0)
content3 = file.readlines()

print(content1,content2,content3,sep='\n\n')

file.close()'''

'''
file = open('sample.txt','w')

file.write("hello Everyone")

file.close()
'''
'''
file = open('sample.txt','a')

file.write("\n welcome to the python class")

file.close()'''

'''
file = open('sample.txt','r+')

file.write("\nFile operations")
file.seek(0)
print(file.read())'''

#same with different approach






import csv


with open('sample.csv','r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)


       # access columns
        

import csv


with open('sample.csv','r') as file:
    content = csv.reader(file)
    for row in content:
        print(row[1])



import csv

with open("sample.csv","w",newline="") as file:


    #json
import json

with open("sample.json", "r") as file:
    data = json








