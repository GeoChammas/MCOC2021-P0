from time import perf_counter
from scipy.linalg import solve, inv
from numpy import eye, ones, logspace, double


def laplaciana(N, tipo=double):
    e = eye(N)-eye(N,N,1)
    return tipo(e+e.T)


Ns = logspace(1, 4, 20)
Ns = [int(x) for x in Ns]

a = open("A_double.txt", "w")


for i in range(10):

    dts =[]
    
    print("Corrida A1 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        x = inv(A)*b
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    


for i in range(10):

    dts =[]
    
    print("Corrida A2 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        x = solve(A,b)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")
    

for i in range(10):

    dts =[]
    
    print("Corrida A3 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        x = solve(A,b, assume_a="pos")
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")


for i in range(10):

    dts =[]
    
    print("Corrida A4 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        x = solve(A,b, assume_a="sym")
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")


for i in range(10):

    dts =[]
    
    print("Corrida A5 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        x = solve(A,b, overwrite_a=True)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")


for i in range(10):

    dts =[]
    
    print("Corrida A6 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        x = solve(A,b, overwrite_b=True)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")


for i in range(10):

    dts =[]
    
    print("Corrida A7 Nº", i+1)
    
    for N in Ns:
        
        A = laplaciana(N)
        b = ones(N)
        
        t1 = perf_counter()
        x = solve(A,b, overwrite_a=True, overwrite_b=True)
        t2 = perf_counter()
        
        dt = t2 -t1
    
        dts.append(dt)
        
    print(f"Tiempo Transcurrido: {dts} s")
    print("")
    a.write(f"{[Ns, dts]}\n")


a.close()
print("LISTO")