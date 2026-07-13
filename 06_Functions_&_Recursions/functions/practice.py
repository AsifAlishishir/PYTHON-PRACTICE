cities=['delhi', 'khulna','dhaka', 'rangpur'];
heros=['thor', 'ironman', 'captain', 'shaktiman','shang-chi'];
def print_len(lists) :
    print(len(lists));

def print_list(lists) :
    for item in lists :
        print(item, end=' ')



# --------------- finding factorial -----------------
# n=int(input("Enter a number: "));

def factorial(num) :
    fact=1
    for i in range(1, num+1) :
        fact*=i;
    return fact;

# res=factorial(n);
# print(res);

# function to turn US dollar into BD taka

# dollar=int(input("Enter dollar Amount: "));

# def dollarToTaka(money):
#     taka=money*123.38;
#     return taka;

# res=dollarToTaka(dollar);
# print("The BDT value of your dollar is:",res);


#function to find odd or even

n=int(input("Enter a number: "));

def oddOrEven(num) :
    if(num%2==0) :
        return """'EVEN.'""";

    else :
        return """'ODD.'""";

res=oddOrEven(n);
print("The given number is:", res);