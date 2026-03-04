product = ['heels','shirts','handbags','laptop','facewash']
search = input("enter the item:")
if search in product:
    print(f'{search} is found!\n Go and shop now!!!')
else:
    print(f'{search} is not found!\n Go for other things')
