def rfun(n):
    if(n>1):
        result=n*rfun(n-1)
        print(result)
    else:
        result=1
    return(result)
rfun(4)

