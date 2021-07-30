result=""
text=input(" Enter your text :")
shift=4
for i in range(len(text)):
    char=text[i]
    if(char.isupper()):
        result+=chr((ord(char)+shift-65)%26+65)
    else:
        result+=chr((ord(char)+shift-97)%26+97)
print(result)