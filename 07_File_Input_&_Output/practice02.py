def check_For_Line():
    word='learning'
    line_no=1
    data=True
    with open('practice.txt', 'r') as f:
        while data:
            data=f.readline()
            if(word in data):
                # print(line_no)
                return line_no
            line_no+=1

    return -1;

print(check_For_Line())