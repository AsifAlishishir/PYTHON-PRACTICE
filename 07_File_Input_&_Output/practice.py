# with open('practice.txt', 'r') as f:
#     # f.write("Hi everyone\nWe are learning file I/O\nusing Java.\nI like programming in Java.")
#     data=f.read();
#     new_data=data.replace('Java', 'Python')
#     print(new_data)

# with open('practice.txt', 'w') as f:
#     f.write(new_data)
with open('practice.txt', 'r') as f:
    data=f.read();
    if 'learning' in data:
        print("Found");
    else:
        print("not found")