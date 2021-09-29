
print("Start")
a,b=1,50
for i in range(a,b+1):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
            break
    if flag==False:
         print(i)
print("finish")

# Check Prime Number Between 1 to 1000
for no in range(2, 1001):
    if no > 1:
        for i in range(2, no):
            if (no % i) == 0:
                break
        else:
            print(no)

"""this is another approach"""
def prime(n1,n2):
    for no in range(n1, n2):
        if no > 1:
            for i in range(n1, no):
                if (no % i) == 0:
                    break
            else:
                print(no)

prime(2,50)