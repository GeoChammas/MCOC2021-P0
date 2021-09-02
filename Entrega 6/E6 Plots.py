import matplotlib.pylab as plt
import ast
from numpy import sqrt

a = open("E6 SOLVE Llena.txt", "r")
a1 = open("E6 SOLVE Dispersa.txt", "r")
a2 = open("E6 INV Llena.txt", "r")
a3 = open("E6 INV Dispersa.txt", "r")


Ns_sl = []
dts_ensamblaje_sl = []
dts_solucion_sl = []


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
    
max_ensamblaje_sl = max(ult_ensamblaje_l)
max_solucion_sl = max(ult_solucion_l)
Ns_sl.append(aux)
dts_ensamblaje_sl.append(aux1)
dts_solucion_sl.append(aux2)

Ns_sl = Ns_sl[0]
dts_ensamblaje_sl = dts_ensamblaje_sl[0]
dts_solucion_sl = dts_solucion_sl[0]



Ns_sd = []
dts_ensamblaje_sd = []
dts_solucion_sd = []


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


max_ensamblaje_sd = max(ult_ensamblaje_d)
max_solucion_sd = max(ult_solucion_d)
Ns_sd.append(aux)
dts_ensamblaje_sd.append(aux1)
dts_solucion_sd.append(aux2)


Ns_sd = Ns_sd[0]
dts_ensamblaje_sd = dts_ensamblaje_sd[0]
dts_solucion_sd = dts_solucion_sd[0]





Ns_il = []
dts_ensamblaje_il = []
dts_solucion_il = []


aux = []
aux1 = []
aux2 = []
ult_ensamblaje_l = []
ult_solucion_l = []

for i in a2:
    sl = ast.literal_eval(i)
    aux.append(sl[0])
    aux1.append(sl[1])
    aux2.append(sl[2])
    ult_ensamblaje_l.append(sl[1][-1])
    ult_solucion_l.append(sl[2][-1])
    
max_ensamblaje_il = max(ult_ensamblaje_l)
max_solucion_il = max(ult_solucion_l)
Ns_il.append(aux)
dts_ensamblaje_il.append(aux1)
dts_solucion_il.append(aux2)

Ns_il = Ns_il[0]
dts_ensamblaje_il = dts_ensamblaje_il[0]
dts_solucion_il = dts_solucion_il[0]


Ns_id = []
dts_ensamblaje_id = []
dts_solucion_id = []

aux = []
aux1 = []
aux2 = []
ult_ensamblaje_d = []
ult_solucion_d = []

for i in a3:
    sl = ast.literal_eval(i)
    aux.append(sl[0])
    aux1.append(sl[1])
    aux2.append(sl[2]) 
    ult_ensamblaje_d.append(sl[1][-1])
    ult_solucion_d.append(sl[2][-1])


max_ensamblaje_id = max(ult_ensamblaje_d)
max_solucion_id = max(ult_solucion_d)
Ns_id.append(aux)
dts_ensamblaje_id.append(aux1)
dts_solucion_id.append(aux2)


Ns_id = Ns_id[0]
dts_ensamblaje_id = dts_ensamblaje_id[0]
dts_solucion_id = dts_solucion_id[0]

a.close()
a1.close()
a2.close()
a3.close()


N0_l = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
N0_d = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

dt_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt0 = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]


# Aquí se arman los O(N^n)

# n=0
x0_ensamblaje_sl = [0, Ns_sl[-1][-1]]
y0_ensamblaje_sl = [max_ensamblaje_sl, max_ensamblaje_sl]
x0_solucion_sl = [0, Ns_sl[-1][-1]]
y0_solucion_sl = [max_solucion_sl, max_solucion_sl]

x0_ensamblaje_sd = [0, Ns_sd[-1][-1]]
y0_ensamblaje_sd = [max_ensamblaje_sd, max_ensamblaje_sd]
x0_solucion_sd = [0, Ns_sd[-1][-1]]
y0_solucion_sd = [max_solucion_sd, max_solucion_sd]


x0_ensamblaje_il = [0, Ns_il[-1][-1]]
y0_ensamblaje_il = [max_ensamblaje_il, max_ensamblaje_il]
x0_solucion_il = [0, Ns_il[-1][-1]]
y0_solucion_il = [max_solucion_il, max_solucion_il]

x0_ensamblaje_id = [0, Ns_id[-1][-1]]
y0_ensamblaje_id = [max_ensamblaje_id, max_ensamblaje_id]
x0_solucion_id = [0, Ns_id[-1][-1]]
y0_solucion_id = [max_solucion_id, max_solucion_id]



# n=1
x1_ensamblaje_sl = [0, Ns_sl[-1][-1]]
y1_ensamblaje_sl = [0, max_ensamblaje_sl]
x1_solucion_sl = [0, Ns_sl[-1][-1]]
y1_solucion_sl = [0, max_solucion_sl]

x1_ensamblaje_sd = [0, Ns_sd[-1][-1]]
y1_ensamblaje_sd = [0, max_ensamblaje_sd]
x1_solucion_sd = [0, Ns_sd[-1][-1]]
y1_solucion_sd = [0, max_solucion_sd]


x1_ensamblaje_il = [0, Ns_il[-1][-1]]
y1_ensamblaje_il = [0, max_ensamblaje_il]
x1_solucion_il = [0, Ns_il[-1][-1]]
y1_solucion_il = [0, max_solucion_il]

x1_ensamblaje_id = [0, Ns_id[-1][-1]]
y1_ensamblaje_id = [0, max_ensamblaje_id]
x1_solucion_id = [0, Ns_id[-1][-1]]
y1_solucion_id = [0, max_solucion_id]



# n=2
x2_ensamblaje_sl = [Ns_sl[-1][-1]*sqrt(0.00001/max_ensamblaje_sl), Ns_sl[-1][-1]]
y2_ensamblaje_sl = [0.00001, max_ensamblaje_sl]
x2_solucion_sl = [Ns_sl[-1][-1]*sqrt(0.00001/max_solucion_sl), Ns_sl[-1][-1]]
y2_solucion_sl = [0.00001, max_solucion_sl]

x2_ensamblaje_sd = [Ns_sd[-1][-1]*sqrt(0.00001/max_ensamblaje_sd), Ns_sd[-1][-1]]
y2_ensamblaje_sd = [0.00001, max_ensamblaje_sd]
x2_solucion_sd = [Ns_sd[-1][-1]*sqrt(0.00001/max_solucion_sd), Ns_sd[-1][-1]]
y2_solucion_sd = [0.00001, max_solucion_sd]


x2_ensamblaje_il = [Ns_il[-1][-1]*sqrt(0.00001/max_ensamblaje_il), Ns_il[-1][-1]]
y2_ensamblaje_il = [0.00001, max_ensamblaje_il]
x2_solucion_il = [Ns_il[-1][-1]*sqrt(0.00001/max_solucion_il), Ns_il[-1][-1]]
y2_solucion_il = [0.00001, max_solucion_il]

x2_ensamblaje_id = [Ns_id[-1][-1]*sqrt(0.00001/max_ensamblaje_id), Ns_id[-1][-1]]
y2_ensamblaje_id = [0.00001, max_ensamblaje_id]
x2_solucion_id = [Ns_id[-1][-1]*sqrt(0.00001/max_solucion_id), Ns_id[-1][-1]]
y2_solucion_id = [0.00001, max_solucion_id]


# n=3
x3_ensamblaje_sl = [Ns_sl[-1][-1]*(0.00001/max_ensamblaje_sl)**(1/3), Ns_sl[-1][-1]]
y3_ensamblaje_sl = [0.00001, max_ensamblaje_sl]
x3_solucion_sl = [Ns_sl[-1][-1]*(0.00001/max_solucion_sl)**(1/3), Ns_sl[-1][-1]]
y3_solucion_sl = [0.00001, max_solucion_sl]

x3_ensamblaje_sd = [Ns_sd[-1][-1]*(0.00001/max_ensamblaje_sd)**(1/3), Ns_sd[-1][-1]]
y3_ensamblaje_sd = [0.00001, max_ensamblaje_sd]
x3_solucion_sd = [Ns_sd[-1][-1]*(0.00001/max_solucion_sd)**(1/3), Ns_sd[-1][-1]]
y3_solucion_sd = [0.00001, max_solucion_sd]


x3_ensamblaje_il = [Ns_il[-1][-1]*(0.00001/max_ensamblaje_il)**(1/3), Ns_il[-1][-1]]
y3_ensamblaje_il = [0.00001, max_ensamblaje_il]
x3_solucion_il = [Ns_il[-1][-1]*(0.00001/max_solucion_il)**(1/3), Ns_il[-1][-1]]
y3_solucion_il = [0.00001, max_solucion_il]

x3_ensamblaje_id = [Ns_id[-1][-1]*(0.00001/max_ensamblaje_id)**(1/3), Ns_id[-1][-1]]
y3_ensamblaje_id = [0.00001, max_ensamblaje_id]
x3_solucion_id = [Ns_id[-1][-1]*(0.00001/max_solucion_id)**(1/3), Ns_id[-1][-1]]
y3_solucion_id = [0.00001, max_solucion_id]



# n=4
x4_ensamblaje_sl = [Ns_sl[-1][-1]*(0.00001/max_ensamblaje_sl)**(1/4), Ns_sl[-1][-1]]
y4_ensamblaje_sl = [0.00001, max_ensamblaje_sl]
x4_solucion_sl = [Ns_sl[-1][-1]*(0.00001/max_solucion_sl)**(1/4), Ns_sl[-1][-1]]
y4_solucion_sl = [0.00001, max_solucion_sl]

x4_ensamblaje_sd = [Ns_sd[-1][-1]*(0.00001/max_ensamblaje_sd)**(1/4), Ns_sd[-1][-1]]
y4_ensamblaje_sd = [0.00001, max_ensamblaje_sd]
x4_solucion_sd = [Ns_sd[-1][-1]*(0.00001/max_solucion_sd)**(1/4), Ns_sd[-1][-1]]
y4_solucion_sd = [0.00001, max_solucion_sd]


x4_ensamblaje_il = [Ns_il[-1][-1]*(0.00001/max_ensamblaje_il)**(1/4), Ns_il[-1][-1]]
y4_ensamblaje_il = [0.00001, max_ensamblaje_il]
x4_solucion_il = [Ns_il[-1][-1]*(0.00001/max_solucion_il)**(1/4), Ns_il[-1][-1]]
y4_solucion_il = [0.00001, max_solucion_il]

x4_ensamblaje_id = [Ns_id[-1][-1]*(0.00001/max_ensamblaje_id)**(1/4), Ns_id[-1][-1]]
y4_ensamblaje_id = [0.00001, max_ensamblaje_id]
x4_solucion_id = [Ns_id[-1][-1]*(0.00001/max_solucion_id)**(1/4), Ns_id[-1][-1]]
y4_solucion_id = [0.00001, max_solucion_id]




plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("SOLVE Matrices Llenas")

for i in range(10):
    plt.loglog(Ns_sl[i],dts_ensamblaje_sl[i], marker="o", markersize = 5, markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_ensamblaje_sl, y0_ensamblaje_sl, color = "royalblue", linestyle='--', label = 'Constante')
plt.loglog(x1_ensamblaje_sl, y1_ensamblaje_sl, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_ensamblaje_sl, y2_ensamblaje_sl, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_ensamblaje_sl, y3_ensamblaje_sl, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_ensamblaje_sl, y4_ensamblaje_sl, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')

plt.ylabel("Tiempo Ensamblaje [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
for i in range(10):
    plt.loglog(Ns_sl[i],dts_solucion_sl[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_solucion_sl, y0_solucion_sl, color = "royalblue", linestyle='--', label = 'Constante')    
plt.loglog(x1_solucion_sl, y1_solucion_sl, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_solucion_sl, y2_solucion_sl, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_solucion_sl, y3_solucion_sl, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_solucion_sl, y4_solucion_sl, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')


plt.ylabel("Tiempo Solución [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xticks(N0_l, N0_l, rotation=45)
plt.legend()
plt.savefig("SOLVE Matrices Llenas", bbox_inches = 'tight')
plt.show()




plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("SOLVE Matrices Dispersas")

for i in range(10):
    plt.loglog(Ns_sd[i],dts_ensamblaje_sd[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_ensamblaje_sd, y0_ensamblaje_sd, color = "royalblue", linestyle='--', label = 'Constante') 
plt.loglog(x1_ensamblaje_sd, y1_ensamblaje_sd, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_ensamblaje_sd, y2_ensamblaje_sd, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_ensamblaje_sd, y3_ensamblaje_sd, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_ensamblaje_sd, y4_ensamblaje_sd, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')
    
plt.ylabel("Tiempo Ensamblaje [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
for i in range(10):
    plt.loglog(Ns_sd[i],dts_solucion_sd[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_solucion_sd, y0_solucion_sd, color = "royalblue", linestyle='--', label = 'Constante')
plt.loglog(x1_solucion_sd, y1_solucion_sd, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_solucion_sd, y2_solucion_sd, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_solucion_sd, y3_solucion_sd, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_solucion_sd, y4_solucion_sd, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')

plt.ylabel("Tiempo Solución [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xticks(N0_d, N0_d, rotation=45)
plt.legend()
plt.savefig("SOLVE Matrices Dispersas", bbox_inches = 'tight')
plt.show()





plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("INV Matrices Llenas")

for i in range(10):
    plt.loglog(Ns_il[i],dts_ensamblaje_il[i], marker="o", markersize = 5, markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_ensamblaje_il, y0_ensamblaje_il, color = "royalblue", linestyle='--', label = 'Constante')
plt.loglog(x1_ensamblaje_il, y1_ensamblaje_il, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_ensamblaje_il, y2_ensamblaje_il, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_ensamblaje_il, y3_ensamblaje_il, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_ensamblaje_il, y4_ensamblaje_il, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')

plt.ylabel("Tiempo Ensamblaje [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
for i in range(10):
    plt.loglog(Ns_il[i],dts_solucion_il[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_solucion_il, y0_solucion_il, color = "royalblue", linestyle='--', label = 'Constante')    
plt.loglog(x1_solucion_il, y1_solucion_il, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_solucion_il, y2_solucion_il, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_solucion_il, y3_solucion_il, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_solucion_il, y4_solucion_il, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')


plt.ylabel("Tiempo Solución [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xticks(N0_l, N0_l, rotation=45)
plt.legend()
plt.savefig("INV Matrices Llenas", bbox_inches = 'tight')
plt.show()




plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("INV Matrices Dispersas")

for i in range(10):
    plt.loglog(Ns_id[i],dts_ensamblaje_id[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_ensamblaje_id, y0_ensamblaje_id, color = "royalblue", linestyle='--', label = 'Constante') 
plt.loglog(x1_ensamblaje_id, y1_ensamblaje_id, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_ensamblaje_id, y2_ensamblaje_id, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_ensamblaje_id, y3_ensamblaje_id, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_ensamblaje_id, y4_ensamblaje_id, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')
    
plt.ylabel("Tiempo Ensamblaje [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
for i in range(10):
    plt.loglog(Ns_id[i],dts_solucion_id[i], marker="o", markersize = 5,  markerfacecolor="k", color = "grey", alpha = 0.5)
plt.loglog(x0_solucion_id, y0_solucion_id, color = "royalblue", linestyle='--', label = 'Constante')
plt.loglog(x1_solucion_id, y1_solucion_id, color = "orange", linestyle='--', label = 'O(N)')
plt.loglog(x2_solucion_id, y2_solucion_id, color = "forestgreen", linestyle='--', label = '$\mathregular{O(N^2)}$')
plt.loglog(x3_solucion_id, y3_solucion_id, color = "r", linestyle='--', label = '$\mathregular{O(N^3)}$')
plt.loglog(x4_solucion_id, y4_solucion_id, color = "purple", linestyle='--', label = '$\mathregular{O(N^4)}$')

plt.ylabel("Tiempo Solución [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xticks(N0_l, N0_l, rotation=45)
plt.legend()
plt.savefig("INV Matrices Dispersas", bbox_inches = 'tight')
plt.show()
