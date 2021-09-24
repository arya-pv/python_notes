lst=[1,45,23,78,98,66,43,56,32,3,6,78,54,32]

def linsearch(lst):
    e=int(input("enter element to search"))
    fla=0
    for i in lst:
        if i==e:
            fla=1
            break
    if fla==0:
        print("not found")
    else:
        print("found")
linsearch(lst)