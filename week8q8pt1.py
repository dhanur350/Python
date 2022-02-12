strng=input()
out=''
for i in strng:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        out=out+i
    else:
        j=ord(i)
        k=j+32
        out=out+chr(k)
print(out)
