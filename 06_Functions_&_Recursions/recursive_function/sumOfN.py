# n=int(input("Enter a number: "));
# sum=0;
# while n>0:
#     remainder=n%10;
#     sum+=remainder;
#     n//=10;

# print(sum);

# now using recursive function

n=int(input("Enter a number: "));

def digitSum(num):
    
    if len(str(num))==1:
        return num;
    else:
        remainder=num%10;
        num=num//10;
        return remainder+digitSum(num);

res=digitSum(n);
print(res);