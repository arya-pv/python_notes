# prime numbers..2,3,5,7,11,...

a=int(input("enter number"))
fla=0
if a>1:
    for i in range(2,a):
        if a%i==0:
            break
    else:
        fla=1
if fla==1:
    print("prime")
else:
    print("not prime")



min=int(input("enter the min"))
max=int(input("enter the max"))
for a in range(min,max+1):
     if a>1:
         for i in range(2,a):
             if a%i==0:
                 break
         else:
             print(a)



