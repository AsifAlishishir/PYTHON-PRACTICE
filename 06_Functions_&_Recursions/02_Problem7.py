l=['asif', 'shishir', 'homer', 'an', 'kishan']

def rem(l, word):
    n=[]
    for item in l:
        if(item != word):
            n.append(item.strip(word))
    return n

print(rem(l, "an"))