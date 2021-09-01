import scipy.sparse as sp
import scipy.sparse.linalg as lin
from scipy.linalg import solve
from numpy import double, ones, eye, logspace
from time import perf_counter


def laplaciana(N, tipo=double):
    e = eye(N)-eye(N,N,1)
    return tipo(e+e.T)


def laplaciana_dispersa(N, t=double):
    return 2*sp.eye(N, dtype = double) - sp.eye(N, N, 1, dtype = double) - sp.eye(N, N, -1, dtype = double)


a = open("E6 SOLVE Llena.txt", "w")
a1 = open("E6 SOLVE Dispersa.txt", "w")


Ns = logspace(1, 4, 40)
Ns = [int(x) for x in Ns]


print("SOLVE Matrices Llenas")
for i in range(10):
    
    dts_ensamblaje_l = []
    dts_solve_l = []
    
    print("Corrida Nº", i+1)
    
    for N in Ns:
    
        t1 = perf_counter()
        A = laplaciana(N)
        b = ones(N, dtype = double)
        Acsr = sp.csr_matrix(A)
        
        t2 = perf_counter()
        
        x = solve(A,b, assume_a="pos")
        
        t3 = perf_counter()
        
        dts_ensamblaje_l.append(t2- t1)
        dts_solve_l.append(t3 - t2)

    print(f"Tiempo Ensamblaje {dts_ensamblaje_l} s")
    print(f"Tiempo Solución {dts_solve_l} s")
    print("")
    a.write(f"{[Ns, dts_ensamblaje_l, dts_solve_l]}\n")


print("")



Ns = logspace(1, 6, 40)
Ns = [int(x) for x in Ns]


print("SOLVE Matrices Dispersas")
for i in range(10):
    
    dts_ensamblaje_d = []
    dts_solve_d = []
    
    print("Corrida Nº", i+1)
    
    for N in Ns:
        
        t1 = perf_counter()
        A = laplaciana_dispersa(N)
        b = ones(N, dtype = double)
        Acsr = sp.csr_matrix(A)
        
        t2 = perf_counter()
        x = lin.spsolve(Acsr, b)
        t3 = perf_counter()

        dts_ensamblaje_d.append(t2- t1)
        dts_solve_d.append(t3 - t2)    

    print(f"Tiempo Ensamblaje {dts_ensamblaje_d} s")
    print(f"Tiempo Solución {dts_solve_d} s")
    print("")
    a1.write(f"{[Ns, dts_ensamblaje_d, dts_solve_d]}\n")


a.close()
a1.close()