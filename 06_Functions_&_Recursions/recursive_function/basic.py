def show(n) :
    if(n==0) :
        return;
    print(n);
    show(n-1);

# show(5)

def countDown(n):
    if(n==0):
        print("Done!"); 
    else:
        print(n);
        countDown(n-1);

# countDown(10)

def sumOfN(n):
    # sum=0;
    if n<=1:
        return n;
    else:
        return n+sumOfN(n-1)

res=sumOfN(10)
print(res)