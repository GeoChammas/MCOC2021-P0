from numpy import zeros, float16, float32, float64
from time import perf_counter
import matplotlib.pylab as plt


Ns = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

dts = []

mems = []

a = open("rendimiento.txt", "w")


for N in Ns:
        

    A = zeros((N, N), dtype=float16)+1
    # uso_memoria_teorico = 4*N*N 
    # uso_memoria_numpy = A.nbytes
    

    B = zeros((N, N))+2
    
    
    t1 = perf_counter()
    C = A@B
    t2 = perf_counter()
    
    uso_memoria_total = A.nbytes + B.nbytes + C.nbytes

    
    dt = t2 - t1
    
    dts.append(dt)
    mems.append(uso_memoria_total)
    
    print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes flop = {N**3/dt} flop/s")
    
    a.write(f"{N} {dt} {uso_memoria_total}\n")

a.close()

