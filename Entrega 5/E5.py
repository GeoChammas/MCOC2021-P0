from numpy import zeros, double, logspace, eye
from time import perf_counter
import matplotlib.pylab as plt
import scipy.sparse as sparse


def laplaciana(N, t=double):
    e = eye(N) - eye(N,N,1)
    return t(e+e.T)


def laplaciana_dispersa(N, t=double):
    return 2*sparse.eye(N, dtype = double) - sparse.eye(N, N, 1, dtype = double) - sparse.eye(N, N, -1, dtype = double)




a = open("E5 MATMUL Llena.txt", "w")
a1 = open("E5 MATMUL Dispersa.txt", "w")


Ns = logspace(1, 6, 30)
Ns = [int(x) for x in Ns]


print("MATMUL Matrices Llenas")
for i in range(10):
    
    dts_ensamblaje_l = []
    dts_solucion_l = []
    
    print("Corrida Nº", i+1)
        
    for N in Ns:
        t1 = perf_counter()
        
        A = laplaciana(N)
        B = laplaciana(N)
        
        t2 = perf_counter()
        
        C = A@B
        
        t3 = perf_counter()
        
        dt_ensamblaje = t2 - t1
        dt_solucion = t3 - t2
        
        dts_ensamblaje_l.append(dt_ensamblaje)
        dts_solucion_l.append(dt_solucion)
        

    print(f"Tiempo Ensamblaje: {dts_ensamblaje_l} s")
    print(f"Tiempo Solución: {dts_solucion_l} s")
    print("")
    a.write(f"{[Ns, dts_ensamblaje_l, dts_solucion_l]}\n")
        
    
    
   
print("")
print("MATMUL Matrices Dispersas")
for i in range(10):
    
    dts_ensamblaje_d = []
    dts_solucion_d = []     
    
    print("Corrida Nº", i+1)
        
    for N in Ns:
        t1 = perf_counter()
        
        A = laplaciana_dispersa(N)
        B = laplaciana_dispersa(N)
        
        Acsr = sparse.csr_matrix(A)
        Bcsr = sparse.csr_matrix(B)
        
        t2 = perf_counter()
        
        C = Acsr@Bcsr
        
        t3 = perf_counter()
        
        dt_ensamblaje = t2 - t1
        dt_solucion = t3 - t2
        
        dts_ensamblaje_d.append(dt_ensamblaje)
        dts_solucion_d.append(dt_solucion)
        
        
    print(f"Tiempo Ensamblaje: {dts_ensamblaje_d} s")
    print(f"Tiempo Solución: {dts_solucion_d} s")
    print("")
    a1.write(f"{[Ns, dts_ensamblaje_d, dts_solucion_d]}\n")
        
    
print("lISTO")
a.close()
a1.close()