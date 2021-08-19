import matplotlib.pylab as plt
import ast



Ns_half = []
dts_half = []
mems_half = []

Ns_single = []
dts_single = []
mems_single = []

Ns_double = []
dts_double = []
mems_double = []

Ns_longdouble = []
dts_longdouble = []
mems_longdouble = []



diccionario = {}
for i in range(3):
    diccionario[f"c{i+1}_h"] = open(f"rendimiento_caso_{i+1}_half.txt", "r")
    diccionario[f"c{i+1}_s"] = open(f"rendimiento_caso_{i+1}_single.txt", "r")
    diccionario[f"c{i+1}_d"] = open(f"rendimiento_caso_{i+1}_double.txt", "r")
    diccionario[f"c{i+1}_ld"] = open(f"rendimiento_caso_{i+1}_longdouble.txt", "r")


for caso in diccionario:
    if caso == "c1_h" or caso == "c2_h" or caso == "c3_h":
        h = diccionario[caso].read().split("\n")
        
        for i in h:
            if len(i)>0:
                sl = ast.literal_eval(i)
                
                Ns_half.append(sl[0])
                dts_half.append(sl[1])
                mems_half.append(sl[2])


    elif caso == "c1_s" or caso == "c2_s" or caso == "c3_s":
        s = diccionario[caso].read().split("\n")
        
        for i in s:
            if len(i)>0:
                sl = ast.literal_eval(i)
                
                Ns_single.append(sl[0])
                dts_single.append(sl[1])
                mems_single.append(sl[2])


    elif caso == "c1_d" or caso == "c2_d" or caso == "c3_d":
        d = diccionario[caso].read().split("\n")
        
        for i in d:
            if len(i)>0:
                sl = ast.literal_eval(i)
                
                Ns_double.append(sl[0])
                dts_double.append(sl[1])
                mems_double.append(sl[2])
                

    elif caso == "c1_ld" or caso == "c2_ld" or caso == "c3_ld":
        ld = diccionario[caso].read().split("\n")
        
        for i in ld:
            if len(i)>0:
                sl = ast.literal_eval(i)
                
                Ns_longdouble.append(sl[0])
                dts_longdouble.append(sl[1])
                mems_longdouble.append(sl[2])


for i in range(3):
    diccionario[f"c{i+1}_h"].close()
    diccionario[f"c{i+1}_s"].close()
    diccionario[f"c{i+1}_d"].close()
    diccionario[f"c{i+1}_ld"].close()



N0 = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

dt_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt0 = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

mem_label = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
mem0 = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]






plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Half")


for i in range(10):
    plt.loglog(Ns_half[i],dts_half[i], color="r")
    plt.scatter(Ns_half[i],dts_half[i], color="r")
    
for i in range(10,20):
    plt.loglog(Ns_half[i],dts_half[i], color="g")
    plt.scatter(Ns_half[i],dts_half[i], color="g")

plt.ylabel("Tiempo Transcurrido [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)

for i in range(10):
    plt.loglog(Ns_half[i],mems_half[i])
    plt.scatter(Ns_half[i],mems_half[i])

plt.axhline(y=8*10**9, color='k', linestyle='--')
plt.ylabel("Uso Memoria [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(mem0, mem_label)
plt.grid(True)
plt.xticks(N0, N0, rotation=45)
plt.savefig("Rendimiento Am1 Half", bbox_inches = 'tight')
plt.show()






plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Single")

for i in range(10):
    plt.loglog(Ns_single[i],dts_single[i], color="c")
    plt.scatter(Ns_single[i],dts_single[i], color="c")

for i in range(10,20):
    plt.loglog(Ns_single[i],dts_single[i], color="r")
    plt.scatter(Ns_single[i],dts_single[i], color="r")
    
for i in range(20,30):
    plt.loglog(Ns_single[i],dts_single[i], color="g")
    plt.scatter(Ns_single[i],dts_single[i], color="g")

plt.ylabel("Tiempo Transcurrido [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)

for i in range(10):
    plt.loglog(Ns_single[i],mems_single[i])
    plt.scatter(Ns_single[i],mems_single[i])

plt.axhline(y=8*10**9, color='k', linestyle='--')
plt.ylabel("Uso Memoria [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(mem0, mem_label)
plt.grid(True)
plt.xticks(N0, N0, rotation=45)
plt.savefig("Rendimiento Am1 Single", bbox_inches = 'tight')
plt.show()





plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Double")

for i in range(10):
    plt.loglog(Ns_double[i],dts_double[i], color="c")
    plt.scatter(Ns_double[i],dts_double[i], color="c")

for i in range(10,20):
    plt.loglog(Ns_double[i],dts_double[i], color="r")
    plt.scatter(Ns_double[i],dts_double[i], color="r")
    
for i in range(20,30):
    plt.loglog(Ns_double[i],dts_double[i], color="g")
    plt.scatter(Ns_double[i],dts_double[i], color="g")

plt.ylabel("Tiempo Transcurrido [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)

for i in range(10):
    plt.loglog(Ns_double[i],mems_double[i])
    plt.scatter(Ns_double[i],mems_double[i])

plt.axhline(y=8*10**9, color='k', linestyle='--')
plt.ylabel("Uso Memoria [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(mem0, mem_label)
plt.grid(True)
plt.xticks(N0, N0, rotation=45)
plt.savefig("Rendimiento Am1 Double", bbox_inches = 'tight')
plt.show()





plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("Rendimiento Am1 Long Double")

for i in range(10):
    plt.loglog(Ns_longdouble[i],dts_longdouble[i], color="r")
    plt.scatter(Ns_longdouble[i],dts_longdouble[i], color="r")

for i in range(10,20):
    plt.loglog(Ns_longdouble[i],dts_longdouble[i], color="g")
    plt.scatter(Ns_longdouble[i],dts_longdouble[i], color="g")
    

plt.ylabel("Tiempo Transcurrido [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)

for i in range(10):
    plt.loglog(Ns_longdouble[i],mems_longdouble[i])
    plt.scatter(Ns_longdouble[i],mems_longdouble[i])

plt.axhline(y=8*10**9, color='k', linestyle='--')
plt.ylabel("Uso Memoria [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(mem0, mem_label)
plt.grid(True)
plt.xticks(N0, N0, rotation=45)
plt.savefig("Rendimiento Am1 Long Double", bbox_inches = 'tight')
plt.show()

