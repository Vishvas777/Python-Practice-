n=int(input("enter a number:"))
if n==2:
    print("this is a prime number")
for i in range(2,n):
    if(n%i==0):
        print("this is a composite nuumber")
        break
    elif n==3:
        print("this is a prime nukmber")
    elif n%3==0:
        print("this is a composite number")
    elif n==3:
        print("this is a prime nukmber")
    else:
        print("this is a prime number ")