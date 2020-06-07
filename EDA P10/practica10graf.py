import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

#Datos de entrada 
x = linspace(0, 5, 20)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, sin(x), marker="o", color="b", linestyle='None')

ax.grid(True)
ax.set_xlabel('x')  #eje x
ax.set_ylabel('y')  #eje y
ax.grid(True)
ax.legend(["y = sen(x)"])

plt.title('Gráfica del seno:')
plt.show()

fig.savefig("grafica.png")
