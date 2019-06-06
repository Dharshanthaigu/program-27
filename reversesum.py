def string(c):
    if len(c)==0:
        return c
    else:
        return string(c[1:])+c[0]
c=input()
print(string(c))
