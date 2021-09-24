k=5
for i in range(6):
    for r in range(0,5):
        print(end=" ")
    k = k + 1
    for j in range(0,6):
        print("*",end=" ")
    print()


def para(n):
    k=n
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k+1
        for j in range(0,n):
            print("*",end=" ")
        print()
para(5)