def power(x,y):
    
    if y==0:
        return 1;
    elif y==1:
        return x;
    else:
        return x*power(x,y-1);

res=power(2,5);
print(res)