def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

nterms=10

print("fibonacci series=")
for i in range(nterms):
    print(fibo(i))