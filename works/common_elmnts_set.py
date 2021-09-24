s1={1,2,3,4,5}
s2={4,5,6,7,8}
common=set()
for i in s1:
    if i in s2:
        common.add(i)
print(common)