import re
with open("donkey.txt", "r") as f:
    data=f.read()
    # print(data)
if "donkey" in data.lower():
        n = re.sub('donkey', '#####', data, flags=re.IGNORECASE)

        with open('donkey.txt', 'w') as f:
            f.write(n)