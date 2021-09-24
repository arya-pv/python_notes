def sum(n):
    s=0
    for i in range(n+1):
        s=s+i
    return s
print(sum(5))


#....without return type...
def sum(n):
     s=0
     for i in range(n+1):
         s=s+i
     print(s)
sum(5)