a=input("enter the string")
b="aeiou"
count=0
for i in a:
    if i in b:
        count=count+1
    else:
        pass
print(count)
