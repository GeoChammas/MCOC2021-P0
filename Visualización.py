import matplotlib.pylab as plt


Ns = []
dts = []
mems = []

a = open("rendimiento.txt", "r")

for line in a:
    sl = line.split()
    N = int(sl[0])
    dt = float(sl[1])
    mem = int(sl[2])
    Ns.append(N)
    dts.append(dt)
    mems.append(mem)


a.close()



dt_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
mem_label = ["1 KB", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]



plt.figure(1)
grafico1 = plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.loglog(Ns,dts)
plt.scatter(Ns,dts)
plt.ylabel("Tiempo Transcurrido [s]")
# grafico1.xaxis.set_major_formatter(plt.NullFormatter())
# plt.xticks(Ns, [])
plt.xticks(color="w")
plt.grid(True)


grafico2 = plt.subplot(2,1,2, sharex = grafico1)
plt.loglog(Ns,mems)
plt.scatter(Ns,mems)
plt.axhline(y=8*10**9, color='k', linestyle='--')
plt.ylabel("Uso Memoria [s]")
plt.xlabel("Tamaño Matriz N")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
