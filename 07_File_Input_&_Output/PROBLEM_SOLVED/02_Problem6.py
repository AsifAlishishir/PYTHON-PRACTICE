with open("log.txt", 'r') as f:
    data=f.read()

if 'python' in data.lower():
    print("Yes it is")
else:
    print("No it's not.")