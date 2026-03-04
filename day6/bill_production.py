# bill geeration

print("Here are the available products:")

data={
    1:{'product':'Rice','price':60},
    2:{'product':'WheatFlour','price':40},
    3:{'product':'Sugar','price':80},
    4:{'product':'Milk','price':25},
    5:{'product':'Eggs (12 pcs)','price':96},
    6:{'product':'Rice','price':60},
    7:{'product':'Rice','price':60},
    8:{'product':'Rice','price':60},
    9:{'product':'Rice','price':60},
    10:{'product':'Rice','price':60},
print("Bill".center(30,'-'))
total_bill=0
s=set()
for i in indexes:
    if i not in s:
        print(f'{data[i]["product"]}{{data[i]["price"]}*{indexes.count(i)}=
