num=input().split()
result=[]
for i in num:
  if i[len(i)-1]!='4':
    result.append(i)
print(*result,end="")