# sets....used to store elements..
#we can store different elements tht is it is hetrogenious
#set doesnot keep order
#set cannot support duplicate elements
#nesting will not allow


a={1,2,3,4,5}
print(a)

b={6,7,8}
print(b)
print(type(b))

#empty set
z=set()
z.add(2)
z.add(4)
z.add(10)
z.add("hello")
z.add(4.7)
z.add(True)
print(z)
print(type(z))

b={9,8,6,1,5,7}  #set doesnot keep order
print(b)

f={1,2,2,3}
print(f)

e={1,5,8,9.4,False,"hello",3}
print(e)
for i in e:
    print(i)