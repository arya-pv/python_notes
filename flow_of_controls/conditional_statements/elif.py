a=int(input("enter the number"))
if a>0:
    print("positive number")
elif a==0:
    print("zero")
else:
    print("negative number")


# if condition1:
#     block content
# elif condition2:
#     block content
# elif condition3:
#     block content
# else:
#     block content


fixed_amount=5000
amount=int(input("enter the amount"))
if amount<=fixed_amount:
    print("balance is",fixed_amount-amount)
else:
    print("insufficient")


num1=int(input("enter first number"))
num2=int(input("enter second number"))
if num1>num2:
    print("num1 is greater")
elif num2>num1:
    print("num2 is greater")
else:
    print("equal")

n01=6
n02=3
n03=3
if n01>n02 and n02==n03:
    print("hello")

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num2&num3:
    print("num1 is greater")
elif num2>num1&num3:
    print("num2 is greater")
elif num1==num2==num3:
    print("all are equal")
else:
    print("num3 is greater")