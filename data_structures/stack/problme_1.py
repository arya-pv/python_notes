stk=[]
size=int(input("enter size"))
top=0
n=0

def  push():
    global top,size
    if (top>size):
        print("stack is full")
    else:
        p=int(input("enter the element to push"))
        stk.append(p)
        top=top+1

def pop():
    global top,size
    if (top<=0):
            print("stack is full")
    else:
            stk.pop()
            top=top-1

def display():
    print(stk)

while (n!=1):
    print("enter the operation want to perform")
    opt=int(input("press 1)push 2)pop 3)display"))
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        display()
    n=int(input("do you want to continue press 1 for exist"))


