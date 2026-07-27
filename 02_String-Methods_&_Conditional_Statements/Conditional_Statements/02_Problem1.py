a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
d=int(input("Enter number:"))

if(a>b and a>c and a>d):
    print("The greatest number is:", a)
elif(b>a and b>c and b>d):
    print("The greatest number is:", b)
elif(c>a and c>b and c>d):
    print("The greatest number is:", c)
else:
    print("The greatest number is:", d)