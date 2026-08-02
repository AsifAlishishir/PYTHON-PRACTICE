# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()

f=open("file.txt", 'r')

for line in f:
    print(line)
f.close()