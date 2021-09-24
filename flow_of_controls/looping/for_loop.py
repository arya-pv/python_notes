#loop...for...while...
# for (variable) in range (number):
#    block content

for i in range(5):  #0,1,2,3,4
    print("hello")


for a in range(2,8):
    print(a)

for i in range(2,10,2):
    print(i)

for i in range(10,2,-2):
    print(i)

min=int(input("enter the minimum range"))
maxi=int(input("enter the maximum range"))
for i in range(min,maxi+1):
    print(i)