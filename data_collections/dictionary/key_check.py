d={1:10, 2:20, 3:30, 4:40, 5:50}
def key_present(x):
     if x in d:
         print(x,'presnt')
     else:
         print(x,'not present')
x=input("enter key")
key_present(x)