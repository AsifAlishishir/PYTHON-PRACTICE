# 01 Write a program to find the sum of first n numbers 
# num= int(input("Enter a number: "));
# i=1;
# sum=0;
# while i <= num:
#     sum+=i;
#     i+=1;

# print(sum);

# 02  Write a program to find the factorial of first n numbers

n=int(input("Enter a number: "));
fact =1;

for i in range(1,n+1) :
    fact*=i;
print("The factorial of",n ,'is:', fact);