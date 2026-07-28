n=int(input("Enter a number:"))
sum=0

if n<1:
    print("Enter a Valid Number!!!")
else:
    for i in range(1,n+1):
        sum+=i
    else:
        print(f"The sum of first {n} natural numbers are: {sum}")