data={
'sathvik' : {'status':True,'python':100,'mysql':99,'softskills':98},
'ravi' : {'status':False,'python':None,'mysql':None,'softskills':None},
'dileep' : {'status':True,'python':70,'mysql':89,'softskills':68},
'praveen' : {'status':True,'python':60,'mysql':68,'softskills':88},
'saaketh' : {'status':True,'python':60,'mysql':79,'softskills':88},
}
user = input("Enter the  student name: ")

if user in data:
    if data[user]['status']:
        sum = data[user]['python']+data[user]['mysql']+data[user]['softskills']
        avg = sum/3
        if avg>80:
            print(f"congrats {user}!!!\n you got 'A' grade")
        elif avg>60:
            print(f"Better luck {user}!!\n you got 'B' grade")
        elif avg>40:
            print(f"Need improvement {user}!!\n you got 'c' grade")
        else:
            print(f"{user},failed in the exam.\n Bring your parents")
        else:
            print(f"{user} didn't write any exams.")
        else:
            print(f"{user} not found")
