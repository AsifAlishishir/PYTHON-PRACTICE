# num=5;

# def calc_Sum(n):
#     if n==0:
#         return 0;
#     else:
#         return n + calc_Sum(n-1);

# res=calc_Sum(num);
# print(res);

li=[1,2,3,4,5];

def printList(l):
    if len(l)==1:
        return l[0];
    else:
        print(l[0]);
        return printList(l[1:len(l)])
        

res=printList(li);
print(res)
