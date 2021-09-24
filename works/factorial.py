num=int(input("enter the number"))
if num>0:
   mul=1
   for i in range(1,num+1):
        mul=mul*i
   print(mul)
if num==0:
    print("factorial of 0 is 1")
else:
    print("factorial doesnot exist for -ve numbers")
