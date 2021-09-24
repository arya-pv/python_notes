#fibunacci series
# 0 1 1 2 3 5 8....

n1=0
n2=1
for i in range(10):
    print(n1)  #..print..n1=0,1,1,2,3,5
    nth=n1+n2  #nth=1,2,3,5,8
    n1=n2      #n1=1,1,2,3,5,
    n2=nth     #n2=1,2,3,5,8
