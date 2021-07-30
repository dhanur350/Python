strng=input()
out=''
for i in strng:
    if ord(i)>=65 and ord(i)<=90:
        j=ord(i)+32
        k=chr(j)
        out=out+k
print(out)
