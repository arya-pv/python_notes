a=input("enter the string")
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print("first recursive character in a is",i)
        break