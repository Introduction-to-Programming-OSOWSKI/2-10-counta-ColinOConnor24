def countA(w):
    letter = 0
    acount = 0
    for i in range(1, len(w) + 1):
        if w[letter] == "a":
            acount += 1
        letter += 1
    return acount