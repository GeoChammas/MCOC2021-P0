import matplotlib.pylab as plt
import ast
from numpy import sqrt

a = open("E5 MATMUL Llena.txt", "r")
a1 = open("E5 MATMUL Dispersa.txt", "r")


Ns_l = []
dts_ensamblaje_l = []
dts_solucion_l = []


aux = []
aux1 = []
aux2 = []
ult_ensamblaje_l = []
ult_solucion_l = []

for i in a:
    sl = ast.literal_eval(i)
    aux.append(sl[0])
    aux1.append(sl[1])
    aux2.append(sl[2])
    ult_ensamblaje_l.append(sl[1][-1])
    ult_solucion_l.append(sl[2][-1])
    
max_ensamblaje_l = max(ult_ensamblaje_l)
max_solucion_l = max(ult_solucion_l)
Ns_l.append(aux)
dts_ensamblaje_l.append(aux1)
dts_solucion_l.append(aux2)

Ns_l = Ns_l[0]
dts_ensamblaje_l = dts_ensamblaje_l[0]
dts_solucion_l = dts_solucion_l[0]


Ns_d = []
dts_ensamblaje_d = []
dts_solucion_d = []


aux = []
aux1 = []
aux2 = []
ult_ensamblaje_d = []
ult_solucion_d = []

for i in a1:
    sl = ast.literal_eval(i)
    aux.append(sl[0])
    aux1.append(sl[1])
    aux2.append(sl[2]) 
    ult_ensamblaje_d.append(sl[1][-1])
    ult_solucion_d.append(sl[2][-1])


max_ensamblaje_d = max(ult_ensamblaje_d)
max_solucion_d = max(ult_solucion_d)
Ns_d.append(aux)
dts_ensamblaje_d.append(aux1)
dts_solucion_d.append(aux2)


Ns_d = Ns_d[0]
dts_ensamblaje_d = dts_ensamblaje_d[0]
dts_solucion_d = dts_solucion_d[0]

a.close()
a1.close()



N0_l = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
N0_d = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

dt_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt0 = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]


# Aquí se arman los O(N^n)

# n=0
x0_ensamblaje_l = [0, Ns_l[-1][-1]]
y0_ensamblaje_l = [max_ensamblaje_l, max_ensamblaje_l]
x0_solucion_l = [0, Ns_l[-1][-1]]
y0_solucion_l = [max_solucion_l, max_solucion_l]

x0_ensamblaje_d = [0, Ns_d[-1][-1]]
y0_ensamblaje_d = [max_ensamblaje_d, max_ensamblaje_d]
x0_solucion_d = [0, Ns_d[-1][-1]]
y0_solucion_d = [max_solucion_d, max_solucion_d]


# n=1
x1_ensamblaje_l = [0, Ns_l[-1][-1]]
y1_ensamblaje_l = [0, max_ensamblaje_l]
x1_solucion_l = [0, Ns_l[-1][-1]]
y1_solucion_l = [0, max_solucion_l]

x1_ensamblaje_d = [0, Ns_d[-1][-1]]
y1_ensamblaje_d = [0, max_ensamblaje_d]
x1_solucion_d = [0, Ns_d[-1][-1]]
y1_solucion_d = [0, max_solucion_d]


# n=2
x2_ensamblaje_l = [Ns_l[-1][-1]*sqrt(0.00001/max_ensamblaje_l), Ns_l[-1][-1]]
y2_ensamblaje_l = [0.00001, max_ensamblaje_l]
x2_solucion_l = [Ns_l[-1][-1]*sqrt(0.00001/max_solucion_l), Ns_l[-1][-1]]
y2_solucion_l = [0.00001, max_solucion_l]

x2_ensamblaje_d = [Ns_d[-1][-1]*sqrt(0.00001/max_ensamblaje_d), Ns_d[-1][-1]]
y2_ensamblaje_d = [0.00001, max_ensamblaje_d]
x2_solucion_d = [Ns_d[-1][-1]*sqrt(0.00001/max_solucion_d), Ns_d[-1][-1]]
y2_solucion_d = [0.00001, max_solucion_d]


# n=3
x3_ensamblaje_l = [Ns_l[-1][-1]*(0.00001/max_ensamblaje_l)**(1/3), Ns_l[-1][-1]]
y3_ensamblaje_l = [0.00001, max_ensamblaje_l]
x3_solucion_l = [Ns_l[-1][-1]*(0.00001/max_solucion_l)**(1/3), Ns_l[-1][-1]]
y3_solucion_l = [0.00001, max_solucion_l]

x3_ensamblaje_d = [Ns_d[-1][-1]*(0.00001/max_ensamblaje_d)**(1/3), Ns_d[-1][-1]]
y3_ensamblaje_d = [0.00001, max_ensamblaje_d]
x3_solucion_d = [Ns_d[-1][-1]*(0.00001/max_solucion_d)**(1/3), Ns_d[-1][-1]]
y3_solucion_d = [0.00001, max_solucion_d]


# n=4
x4_ensamblaje_l = [Ns_l[-1][-1]*(0.00001/max_ensamblaje_l)**(1/4), Ns_l[-1][-1]]
y4_ensamblaje_l = [0.00001, max_ensamblaje_l]
x4_solucion_l = [Ns_l[-1][-1]*(0.00001/max_solucion_l)**(1/4), Ns_l[-1][-1]]
y4_solucion_l = [0.00001, max_solucion_l]

x4_ensamblaje_d = [Ns_d[-1][-1]*(0.00001/max_ensamblaje_d)**(1/4), Ns_d[-1][-1]]
y4_ensamblaje_d = [0.00001, max_ensamblaje_d]
x4_solucion_d = [Ns_d[-1][-1]*(0.00001/max_solucion_d)**(1/4), Ns_d[-1][-1]]
y4_solucion_d = [0.00001, max_solucion_d]




plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("MATMUL Matrices Llenas")

for i in range(10):
    plt.loglog(Ns_l[i],dts_ensamblaje_l[i], marker="o", markersize = 5, markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_ensamblaje_l, y0_ensamblaje_l, color = "royalblue", linestyle='--', label = 'Constante')
plt.loglog(x1_ensamblaje_l, y1_ensamblaje_l, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_ensamblaje_l, y2_ensamblaje_l, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_ensamblaje_l, y3_ensamblaje_l, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_ensamblaje_l, y4_ensamblaje_l, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')

plt.ylabel("Tiempo Ensamblaje [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
for i in range(10):
    plt.loglog(Ns_l[i],dts_solucion_l[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_solucion_l, y0_solucion_l, color = "royalblue", linestyle='--', label = 'Constante')    
plt.loglog(x1_solucion_l, y1_solucion_l, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_solucion_l, y2_solucion_l, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_solucion_l, y3_solucion_l, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_solucion_l, y4_solucion_l, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')


plt.ylabel("Tiempo Solución [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xticks(N0_l, N0_l, rotation=45)
plt.savefig("MATMUL Matrices Llenas", bbox_inches = 'tight')
plt.legend()
plt.show()




plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("MATMUL Matrices Dispersas")

for i in range(10):
    plt.loglog(Ns_d[i],dts_ensamblaje_d[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_ensamblaje_d, y0_ensamblaje_d, color = "royalblue", linestyle='--', label = 'Constante') 
plt.loglog(x1_ensamblaje_d, y1_ensamblaje_d, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_ensamblaje_d, y2_ensamblaje_d, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_ensamblaje_d, y3_ensamblaje_d, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_ensamblaje_d, y4_ensamblaje_d, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')
    
plt.ylabel("Tiempo Ensamblaje [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
for i in range(10):
    plt.loglog(Ns_d[i],dts_solucion_d[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_solucion_d, y0_solucion_d, color = "royalblue", linestyle='--', label = 'Constante')
plt.loglog(x1_solucion_d, y1_solucion_d, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_solucion_d, y2_solucion_d, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_solucion_d, y3_solucion_d, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_solucion_d, y4_solucion_d, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')

plt.ylabel("Tiempo Solución [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xticks(N0_d, N0_d, rotation=45)
plt.savefig("MATMUL Matrices Dispersas", bbox_inches = 'tight')
plt.legend()
plt.show()