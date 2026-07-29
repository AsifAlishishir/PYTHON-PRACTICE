def greatest(a=1,b=1,c=1):
    if(a>b and a>c):
        print(f"{a} is the greatest.")
    elif(b>a and b>c):
        print(f"{b} is the greatest.")
    else:
        print(f"{c} is the greatest.")

first=int(input("Enter first number: "))
second=int(input("Enter second number: "))
third=int(input("Enter third number: "))

greatest(first,second,third)