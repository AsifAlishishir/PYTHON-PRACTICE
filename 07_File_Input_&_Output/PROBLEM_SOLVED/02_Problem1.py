with open('poems.txt', 'r') as f:
    data=f.read()
    if("twinkle".lower() in data):
        print("Twinkle is present in the content!")
    else:
        print("Twinkle is not present in the content!")