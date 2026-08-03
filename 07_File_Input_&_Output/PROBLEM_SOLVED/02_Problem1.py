with open('poems.txt', 'r') as f:
    data=f.read()
    if("twinkle" in data.lower()):
        print("Twinkle is present in the content!")
    else:
        print("Twinkle is not present in the content!")