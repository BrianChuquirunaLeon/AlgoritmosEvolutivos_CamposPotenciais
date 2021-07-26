import numpy as np
import matplotlib.pyplot as plt

x,average,best_average_fitness,ind0,ind1,ind2,ind3,ind4,ind5,ind6,ind7,ind8,ind9,best_actual_average,best_actual = np.loadtxt('datos_5.txt',usecols=[0,1,2,8,9,10,11,12,13,14,15,16,17,18,19],unpack=True)


plt.title("Best actual vs. Average of each generation")
plt.plot(x,average,"r-o",color='black',linewidth=3,label='average_fitness')
plt.plot(x,best_actual,"r-o",color='red',linewidth=3,label='best_actual')
plt.show()


plt.plot(x,ind0,"r",color='cyan',linewidth=1,label='ind0')
plt.plot(x,ind1,"r",color='black',linewidth=1,label='ind1')
plt.plot(x,ind2,"r",color='magenta',linewidth=1,label='ind2')
plt.plot(x,ind3,"r",color='yellow',linewidth=1,label='ind3')
plt.plot(x,ind4,"r",color='gray',linewidth=1,label='ind4')
plt.plot(x,ind5,"r",color='aquamarine',linewidth=1,label='ind5')
plt.plot(x,ind6,"r",color='purple',linewidth=1,label='ind6')
plt.plot(x,ind7,"r",color='pink',linewidth=1,label='ind7')
plt.plot(x,ind8,"r",color='brown',linewidth=1,label='ind8')
plt.plot(x,ind9,"r",color='orange',linewidth=1,label='ind9')
plt.plot(x,average,"r",color='green',linewidth=3,label='average_fitness')
plt.show()

