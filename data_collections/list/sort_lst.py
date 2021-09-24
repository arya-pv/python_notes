# inbuild method

lst=[4,6,0,-7,9,1,-45,89]
lst.sort()
print(lst)

# without inbuild method
my_list=[2,5,0,-5,-87,432,-865,111,787]
new_list=[]

while my_list:
    min=my_list[0]
    for i in my_list:
        if i<min:
            min=i
    new_list.append(min)
    my_list.remove(min)

print(new_list)
print(my_list)

