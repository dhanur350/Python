def xyz(a,b):
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a
    if a == 1:
        return b
    return a+xyz(a,b-1)
print(xyz(2,12))

