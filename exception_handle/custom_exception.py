a=int(input("enter num"))
b=int(input("enter num"))
if b>a:
    raise Exception("no2 is greater")
else:
    print(a/b)


age=int(input("enter age"))
n=45
if age>n:
    raise Exception("not eligible")
else:
    print("you are eligible")