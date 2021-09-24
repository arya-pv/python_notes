#while(condition):
#    body of loop
#    incr/decr


a=0
while a<=10:
    print("hello")
    a=a+1


a=10
while a>0:
    print(a)
    a=a-1

min=int(input("enter min number"))
max=int(input("enter max number"))
while min<=max:
    if min%2==0:
        print(min)
    min=min+1


while True:  # use for infinite output
    print("hello")