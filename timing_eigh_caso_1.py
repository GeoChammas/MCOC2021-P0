from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import eigh, inv
from numpy import eye, float32, ones

def laplaciana(N, tipo=float32):
    e = eye(N)-eye(N,N,1)
    return tipo(e+e.T)


N = 10

A = laplaciana(N)
b = ones(N)


t1 = perf_counter()

w,h = eigh(A, driver = "evx", overwrite_a = False)

t2 = perf_counter()

dt = t2 -t1

print(f"Tiempo Transcurrido: {dt} s")
