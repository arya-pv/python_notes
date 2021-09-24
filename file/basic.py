#file--read(r) and write(w)
#read
f1=open("read", "r")
for i in f1:
    print(i)

#write

f1=open("write", "w") #if we give the file name which is not presnt it itself make new file and put it
f1.write("puthurkara")

#w+ or r+ means reading and writing


f0=open("aaa","r")
f3=open("aaacopy","w")
for i in f0:
    f3.write(i)