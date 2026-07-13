# l=[1,2,3,4];
# sum=0;
# i=0;
# for i in range(0, len(l)):
#     sum+=l[i];

# print(sum);

# using recursive function

l=[1,2,3,4];

def sumOfList(lists):
    if(len(lists)==1):
        return lists[0];
    else:
        return lists[-1]+ sumOfList(lists[:-1]);

res=sumOfList(l);
print(res);