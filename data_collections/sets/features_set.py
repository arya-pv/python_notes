# 1.not keeping order
# 2.not support duplicate elements
# 3.hetrogeneous
# 4.mutable
# 5.nesting not possible

#nesting example

# a={1,{2,3}}
# print(a)


a={1,2,3,4,5,6,7}
b={3,5,4,7,8,9,0}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b)) #a-b
print(b.difference(a)) #b-a

