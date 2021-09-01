from numpy import zeros, float16, float32, float64, logspace
from time import perf_counter
import matplotlib.pylab as plt


#Ns = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
Ns = logspace(0, 4, 30)



dts = []

mems = []

a1 = open("rendimiento1.txt", "w")
a2 = open("rendimiento2.txt", "w")
a3 = open("rendimiento3.txt", "w")
a4 = open("rendimiento4.txt", "w")
a5 = open("rendimiento5.txt", "w")
a6 = open("rendimiento6.txt", "w")
a7 = open("rendimiento7.txt", "w")
a8 = open("rendimiento8.txt", "w")
a9 = open("rendimiento9.txt", "w")
a10 = open("rendimiento10.txt", "w")

archivos = []
archivos.extend([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10])


for a in range(len(archivos)):
    
    print("Rendimiento Nº", a+1)
    
    for N in Ns:
            
        N = int(N)
        
        A = zeros((N, N))+1        
    
        B = zeros((N, N))+2
        
        
        t1 = perf_counter()
        C = A@B
        t2 = perf_counter()
        
        uso_memoria_total = A.nbytes + B.nbytes + C.nbytes
    
        
        dt = t2 - t1
        
        dts.append(dt)
        mems.append(uso_memoria_total)
        
        print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes flop = {N**3/dt} flop/s")

        archivos[a].write(f"{N} {dt} {uso_memoria_total}\n")

    print("")



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