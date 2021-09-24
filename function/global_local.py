x=5

def foo():
    x=3
    x=x+10
    print("local x=",x)

foo()
print("global x=",x)




x = 5

def foo():
    global x
    x = x + 10
    print("local x=", x)


foo()
print("global x=", x)
