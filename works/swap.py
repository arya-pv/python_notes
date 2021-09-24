no1=int(input("enter no1"))
no2=int(input("enter no2"))

print("value b4 swapping no1=",no1)#5
print("value b4 swapping no2=",no2)#4

# temp=no1 #temp=5
# no1=no2  #no1=4
# no2=temp #no2=5

#second approach
#(no1,no2)=(no2,no1)

#third approach
#no1=5,no2=2

no1=no1+no2  # no1=7
no2=no1-no2  #no2=5
no1=no1-no2  #no1=2


print("value after swapping no1=",no1)
print("value after swapping no2=",no2)