from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import eigh, inv
from numpy import eye, double, ones, logspace


def laplaciana(N, tipo=double):
    e = eye(N)-eye(N,N,1)
    return tipo(e+e.T)


Ns = logspace(1, 3.7, 20)
Ns = [int(x) for x in Ns]

a = open("B_double.txt", "w")


for i in range(10):

    dts =[]
    
    print("Corrida B1 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w, h = eigh(A)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    


for i in range(10):

    dts =[]
    
    print("Corrida B2_F Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "ev", overwrite_a = False)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    
    
    
for i in range(10):

    dts =[]
    
    print("Corrida B2_T Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "ev", overwrite_a = True)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    
    

for i in range(10):

    dts =[]
    
    print("Corrida B3_F Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "evd", overwrite_a = False)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    
    

for i in range(10):

    dts =[]
    
    print("Corrida B3_T Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "evd", overwrite_a = True)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")



for i in range(10):

    dts =[]
    
    print("Corrida B4_F Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "evr", overwrite_a = False)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    


for i in range(10):

    dts =[]
    
    print("Corrida B4_T Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "evr", overwrite_a = True)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")



for i in range(10):

    dts =[]
    
    print("Corrida B5_F Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "evx", overwrite_a = False)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    


for i in range(10):

    dts =[]
    
    print("Corrida B5_T Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        w,h = eigh(A, driver = "evx", overwrite_a = True)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    
    
a.close()
print("LISTO")