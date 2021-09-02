import scipy.sparse as sp
import scipy.sparse.linalg as lin
from numpy import double, logspace, eye
from time import perf_counter
from scipy.linalg import inv

def laplaciana(N, tipo=double):
    e = eye(N)-eye(N,N,1)
    return tipo(e+e.T)

def laplaciana_dispersa(N, t=double):
    return 2*sp.eye(N, dtype = double) - sp.eye(N, N, 1, dtype = double) - sp.eye(N, N, -1, dtype = double)



a = open("E6 INV Llena.txt", "w")
a1 = open("E6 INV Dispersa.txt", "w")

Ns = logspace(1, 4, 30)
Ns = [int(x) for x in Ns]


print("INV Matrices Llenas")
for i in range(10):
    
    dts_ensamblaje_l = []
    dts_solve_l = []
    
    print("Corrida Nº", i+1)
    
    for N in Ns:
    
        t1 = perf_counter()
        A = laplaciana(N)
        
        t2 = perf_counter()
        
        Am1 = inv(A, overwrite_a = True)
        
        t3 = perf_counter()
        
        dts_ensamblaje_l.append(t2- t1)
        dts_solve_l.append(t3 - t2)

    print(f"Tiempo Ensamblaje {dts_ensamblaje_l} s")
    print(f"Tiempo Solución {dts_solve_l} s")
    print("")
    a.write(f"{[Ns, dts_ensamblaje_l, dts_solve_l]}\n")


print("")



print("INV Matrices Dispersas")
for i in range(10):
    
    dts_ensamblaje_d = []
    dts_solve_d = []
    
    print("Corrida Nº", i+1)
    
    for N in Ns:
        
        t1 = perf_counter()
        A = laplaciana_dispersa(N)
        Acsc = sp.csc_matrix(A)
        
        t2 = perf_counter()
        Am1 = lin.inv(Acsc)
        t3 = perf_counter()

        dts_ensamblaje_d.append(t2- t1)
        dts_solve_d.append(t3 - t2)    

    print(f"Tiempo Ensamblaje {dts_ensamblaje_d} s")
    print(f"Tiempo Solución {dts_solve_d} s")
    print("")
    a1.write(f"{[Ns, dts_ensamblaje_d, dts_solve_d]}\n")

a.close()
a1.close()