n=int(input("Enter a number:"))
i=1
sum=1
while (i<=n):
    print("i",i)
    sum*=i
    print("sum",sum)
    i+=1

print(f"The factorial of {n} is : {sum}")
