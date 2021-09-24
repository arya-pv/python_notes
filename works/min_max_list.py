a=[7,9,11,15,1,2,3,4,5]
a.sort()
print(a)
print("minimum",a[0])
print("maximum",a[-1])


b=[1,2,3,4,5]
c=[]
for i in b:
    s=i*5
    c.append(s)
print(c)


#second method

numbers=[1,2,3,4,5,6,7,8,3,5,6,78]
s=[n*5 for n in numbers]  #we can add for if by using space in one line
print(s)


