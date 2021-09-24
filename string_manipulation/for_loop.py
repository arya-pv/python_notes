for i in "abcd":
 print(i)


a="arya"
for i in a:
    print(i)

a="abcd"
b="acfr"
for i in a:
    if i in b:  #in means == and not in means not equal to
        print(i)

a="luminar"
b=""
for i in a:
    b=b+i
print("b=",b)

b="arya"
a=input("enter the element")
for i in a:
    if i in b:
        print("present",i)
    else:
        print("not present")


a="malayalam"
e=input("enter element to count")
count=0
for i in a:
    if i in e:
        count=count+1
print(count)



