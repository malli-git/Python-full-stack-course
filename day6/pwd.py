# password validation using spl,upper,lower,digit cases


pwd = input("Enter the password: ")

if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("splchar")
    if len(s)==4:
        print("Strong password")
    else:
        print("weak password.password needs to have uppercase,lowercase,splchar,digit")
else:
    print("length needs to be >=8")
        
