# exception as ...will print what is the exception is

lst=[1,2,3,4]
index=int(input("enter index"))
try:
    print(lst[index])
except Exception as e:
    print(e.args)
finally:
    print("inside")


num1=int(input("enter num"))
num2=int(input("enter num"))
try:
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)

#one try for one Exception as..for different operations there is different exception as