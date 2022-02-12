t=input().split()
s=[]
for e in t:
  if int(e) not in s:
    s.append(int(e))
if len(s)>1:
  ans=sorted(s)
  print(ans[1]+ans[-2],end="")
else:
  print(s[0]*2,end="")