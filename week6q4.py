num1=int(input())
num2=int(input())
i=1
while(i<=num1 and i<=num2):
    if(num1%i==0 and num2 %i ==0):
        output=i
    i=i+1

print(output)
