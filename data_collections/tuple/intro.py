#bracket is not mandotory
#immutable means cannot add or remove
#it keeps order
#allows duplication
#hetrogeneous
#nesting possible

tup1=1,2,3,4,10,6,9,-2,3,3,4
print(tup1)
print(type(tup1))

tup2=1,3,6,2,"hello",(8,4,5)  #nesting possible
print(tup2)

tup3=1,6,3,True,"hi",9,3
for i in tup3:
    print(i)