Estimates=[100,200,200,300,200,220,250,400,450,430,350,300,300,300,300,300,200,220,220,220,100,150,170,1000,1783,1000,900,700,500,800,900]
Estimates.sort()
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:]
for i in range(len(Estimates)):
    print(Estimates)