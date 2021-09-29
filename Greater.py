a,b,c=10,30,80
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
    
#Function Approach
def greater(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print("n1 is greater",n1)
    elif n2 > n3:
        print("b is greater",n2)
    else:
        print("n3 is greater",n3)

greater(10,20,30)
