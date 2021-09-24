def add(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation")
print("1.add")
print("2.subtraction")
print("3.multiply")
print("4.divide")
while True:
    choice=int(input("enter choice"))
    num1=float(input("enter number"))
    num2=float(input("enter number"))
    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(subtraction(num1,num2))
    elif choice==3:
        print(multiply(num1,num2))
    elif choice==4:
        print(divide(num1,num2))
    else:
        print("invalid choice")
