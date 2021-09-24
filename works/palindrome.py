#palindrome...eg..malayalam

a="abcd"
b=a[::-1]
print(b)

a=input("enter the word")
b=a[::-1]
print(b)
if a==b:
    print("palindrome")
else:
    print("not palindrome")