import re

words = ["donkey", "horse", "cow", "goat"]

with open("donkey.txt", 'r') as f:
    data=f.read()

for word in words:
    data=re.sub(word, '#'*len(word), data, flags=re.IGNORECASE)

with open("donkey.txt", 'w') as f:
    f.write(data)