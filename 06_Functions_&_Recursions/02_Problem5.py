num=int(input("Enter a number: "))
def star(n):
    if n==0:
        return
    else:
        print("*"*n)
        star(n-1)

star(num)