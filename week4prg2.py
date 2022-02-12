def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    return(f)
m=int(input())
n=int(input())
if(m+n>20 or n==m):
  print("invalid",end="")
elif(n>0):
  print(int(fact(m+1)/fact(m+1-n)*fact(m)),end="")