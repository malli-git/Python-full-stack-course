'''
for var in seq:
  stmts
seq: list,tuple,set,dict,str,range
'''
Products = ['bread','butter','milk','sugar','salt']

for Product in Products:
    print(f'{Products}- Add to fav|Buy now| Add to cart')
          
sizes = ('xs','s','m','l','xl','xxl','xxl')
for s in sizes:
    print(f'...|{s}|... ')



followers = {'ysr','mallikarjuna reddy','kcr','ysj','maheshbabau'}
for F in followers:
    print(f'{F}-|follow Back|remove|message|')




data={
'varsha':['c','puthon','java'],
'saaketh':['ml','al','python'],
'meghana':['java','linux','python'],
'sirisha':['figma','uxui','python'],
}

for i in data:
    print(f'{i}:{data[i]}')
    
s='python programming'

for i in s:
    print(f'{i}')


#range(start,stop+1,step) = range(0,n,1)

for i in range(1,11):
  print(i)
 #eg
n=11
for i in range(1,n):
    print(i)

for i in range (1,100,1):
    print(i)

for i in range (1,100,2):
    print(i)


for i in range(10,0,-1):
    print(i)



n=int(input("Enter the number: "))

print(f"{n}: Table")
for i in range(1,11):
      print(f"{n}*{i}={n*i}")


for i in range(1,10):
    if i==7:
        continue
    print(i)


for i in range(1,10):
    if i==7:
        break
    print(i)



























    
