#1
d = {"Arjun": 85, "Rahul": 90,"Anita": 78}
name = input("Enter student name: ").strip()
try:
    print(d[name])
except KeyError:
    print("student not found!")
#2

s1 = set(map(int,input("enter elements of set 1: ").split()))
s2 = set(map(int,input("enter elements of set 2: ").split()))

print(f'union: {s1|s2}')
print(f'intersection: {s1 & s2}')
print(f'difference(set1 - set2):{s1-s2}')

#3
try:
    with open('data.txt','r') as file:
        print(len(file.readlines()))
except FileNotFoundError:
    print('data.txt does not exist')

#4

import json

with open('demojson.json','w') as  file:
    data = [
        {'title': 'python Basics','author':'john deo','price':1250},
        {'title': 'HTML Basics','author':'john deo','price':1250},
        {'title': 'JAVA Basics','author':'john deo','price':1250},
        {'title': 'MYSQL Basics','author':'john deo','price':1250}
        ]
    json.dump(data,file,indent=4)

with open('demo2.json','r') as file:
    print(json.load(file))

#5

try:
    file = open("data.txt",'r')
    print(file.read())

except FileNotFoundError:
    print("File is not found")
