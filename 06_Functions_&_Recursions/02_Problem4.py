num=int(input("Enter a number: "))

def sum(n):
    if n<=0:
        return "Please Enter a valid Number!"
    else:
        if n==1:
            return 1;
        else:
            return n+sum(n-1)

result=sum(num)
print(result)