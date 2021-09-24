count={}
data=input("enter")
words=data.split(" ")
# print(words)
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val=val+1
        count.update({word:val})
print(count)