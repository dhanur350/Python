def GCD (m,n):
  if m%n==0:
    return(n)
  else:
    return(GCD(n,m%n))
m=int(input())
n=int(input())
print(GCD(m,n),end="")