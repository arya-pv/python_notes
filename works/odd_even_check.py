num=int(input("enter the number"))
if num>0:
   if num%2==0 & num>0:
      print("number is even")
   else:
        print("number is odd")
else:
    print("enter a positive number")


min=int(input("enter minimum range"))
maxi=int(input("enter maximum range"))
for i in range(min,maxi+1):
    if i%2==0:
      print(i)