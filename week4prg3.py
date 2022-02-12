n=int(input())
prev=0
for i in range(1,n+1):
  for j in range(1,i+1):
    prev=prev+1
    ans=prev**2
    if i==j :
      print(ans,end="")
    else:
      print(ans,"",end="")
  if i!=n:
    print(" ")