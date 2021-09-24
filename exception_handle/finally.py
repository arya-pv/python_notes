#finally block is a part of exception handling and is not very important
#try block works full time and finally block works only finally run and exception run when exception call

a=[1,2,3,4]
index=int(input("enter index"))
try:
    print(a[index])
except:
    print("index not exist")
finally:
    print("inside finally")