num=int(input("Enter a number: "))

def mul_Table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

mul_Table(num)