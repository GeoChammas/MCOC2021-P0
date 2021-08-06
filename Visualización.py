import matplotlib.pylab as plt


Ns = []
dts = []
mems = []


a1 = open("rendimiento1.txt", "r")
a2 = open("rendimiento2.txt", "r")
a3 = open("rendimiento3.txt", "r")
a4 = open("rendimiento4.txt", "r")
a5 = open("rendimiento5.txt", "r")
a6 = open("rendimiento6.txt", "r")
a7 = open("rendimiento7.txt", "r")
a8 = open("rendimiento8.txt", "r")
a9 = open("rendimiento9.txt", "r")
a10 = open("rendimiento10.txt", "r")

archivos = []
archivos.extend([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10])

for a in range(len(archivos)):
    
    Nss = []
    dtss = []
    memss = []
    
    for line in archivos[a]:
        sl = line.split()
        N = int(sl[0])
        dt = float(sl[1])
        mem = int(sl[2])
        Nss.append(N)
        dtss.append(dt)
        memss.append(mem)
        
    Ns.append(Nss)
    dts.append(dtss)
    mems.append(memss)


a1.close()
a2.close()
a3.close()
a4.close()
a5.close()
a6.close()
a7.close()
a8.close()
a9.close()
a10.close()


N0 = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

dt_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt0 = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]

mem_label = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]
mem0 = [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]


plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("Rendimiento A@B")

for i in range(len(archivos)):
    plt.loglog(Ns[i],dts[i])
    plt.scatter(Ns[i],dts[i])
    
plt.ylabel("Tiempo Transcurrido [s]")
plt.xticks(visible=False)
plt.yticks(dt0, dt_label)
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
plt.loglog(Ns[0],mems[0])
plt.scatter(Ns[0],mems[0])
plt.axhline(y=8*10**9, color='k', linestyle='--')
plt.ylabel("Uso Memoria [s]")
plt.xlabel("Tamaño Matriz N")
plt.yticks(mem0, mem_label)
plt.grid(True)
plt.xticks(N0, N0, rotation=45)
plt.savefig('Rendimiento A@B.png')
plt.show()

