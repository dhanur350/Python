import statistics
import matplotlib.pyplot as plt
Estimates=[100,200,200,300,200,220,250,400,450,430,350,300,300,300,300,300,200,220,220,220,100,150,170,1000,1783,1000,900,700,500,800,900,900,800,600,750,750,560,400,1000]
y=[]
Estimates.sort()
tv=int(0.1*(len(Estimates)))
Estimates=Estimates[tv:]
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot([375],[5],'g^')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.show()