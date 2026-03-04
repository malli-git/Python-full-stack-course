# function

def Student_data(info):
    print(f'Name:{info[0]}')
    print(f'Course:{info[1]}')
    print(f'Gar_year:{info[2]}')
    print("-----End------")


data = [['varsha','PFS','2026'],
        ['Saaketh','JFS','2026'],
        ['Dileep','DA','2026'],
        ['Sirisha','DS','2026'],
        ]

for i in data:
    Student_data(i)

#display positions
def display(uname,email,password):
    print(f'Username:{uname}')
    print(f'Email:{email}')
    print(f'Password:{password}')


display('Varsha','Varsha@gmail.com','Varsha@123')
display('Varsha@123','Varsha','Varsha@gmail.com')
display('Varsha@gmail.com','Varsha@123','Varsha')



#key word
def display(uname,email,password):
    print(f'Username:{uname}')
    print(f'Email:{email}')
    print(f'Password:{password}')


display(uname='Varsha',email='Varsha@gmail.com',password='Varsha@123')
display(password='Varsha@123',uname='Varsha',email='Varsha@gmail.com')
display(email='Varsha@gmail.com',password='Varsha@123',uname='Varsha')


# default arguments
def display(uname,email,password,status='Absent'):
    print(f'Username:{uname}')
    print(f'Email:{email}')
    print(f'Password:{password}')
    print(f'status:{status}')

display('Varsha','Varsha@gmail.com','Varsha@123','present')


#variable length

def display(*name):
    for i in name:
        print(i)
    else:
            print("------End of the list------")



display('K mallikarjuna reddy')
display('malli','arjuna','reddy')
display('kmr','ker','kcr')
