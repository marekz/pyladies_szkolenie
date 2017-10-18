def xo_checker(zdanie):

    lx = 0
    lo = 0

    for znak in zdanie:
        if znak == "o":
            lo = lo + 1
        elif znak == "x":
            lx = lx + 1
        else:
            print("Illegal letters in text")
            exit()


    if(lx == lo):
        return True
    else:
        return False


print(xo_checker("xoxoxoxoxoxoxoxoxo"))
print(xo_checker("xoxoxoxoxoxoxoxoxoooooo"))
print(xo_checker("1xoxoxoxoxoxoxoxoxoooooo"))
