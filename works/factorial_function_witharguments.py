def fact(num):
    mul=1
    if num>0:
      for i in range(1,num+1):
         mul=mul*i
      print(mul)
    elif num==0:
        print("factorial of 0 is 1")
    else:
        print("factorial doesnot exist for -ve num")

fact(5)
fact(10)
fact(0)
fact(-5)