from time import perf_counter
from numpy import zeros
from numpy import half, single, double, longdouble, logspace
from scipy.linalg import inv


def laplaciana(N, dtype):
    A = zeros((N,N), dtype=dtype)
    
    for i in range(N):
        for j in range(max(0,i-2), i):
            A[i,i] = 2
            if abs(i-j) == 1:
                A[i,j] = -1
                A[j,i] = -1
    
    return A



Ns = logspace(1, 4, 20)
Ns = [int(x) for x in Ns]
dts = []
mems = []


a = open("rendimiento_caso_2_longdouble.txt", "w")


for i in range(10):
    
    dts = []
    mems = []
    
    print("Corrida Nº", i+1)
    for N in Ns:
        
        N = int(N)
        
        A = laplaciana(N, dtype=longdouble)
             
        t1 = perf_counter()
        Am1 = inv(A, overwrite_a = False)
        t2 = perf_counter()
        
        dt_inversion = t2 - t1
        
        bytes_total = A.nbytes + Am1.nbytes
        
        dts.append(dt_inversion)
        mems.append(bytes_total)
        
    print(f"Tiempo inversión: {dts} s") 
    print(f"Uso Memoria: {mems} bytes")
    print("")
        
    a.write(f"{[Ns, dts, mems]}\n")
        

    
a.close()
print("LISTO")