# 1
# 2 3
# 4 5 6
# 7 8 9 10

def pattern(n):
    num=1
    for i in range(n):
        for j in range(i):
            print(num,end=" ")
            num=num+1
        print()
pattern(5)