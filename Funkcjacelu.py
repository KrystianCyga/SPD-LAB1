from RandomNumberGenerator import *
import numpy as np
import math
import random
# r czas przygotowania
# p czas wykonania
# q czas stygniecia

def calculate(perm, r, p, q):
    n = len(perm)
    S = [0]*n
    C = [0]*n
    harm=[0]*n
    Cmax = 0
    S[0] = r[perm[0]]
    C[0] = S[0] + p[perm[0]]
    Cmax = C[0] + q[perm[0]]
    harm[0]=[S[0],C[0],C[0]+q[0]]
    for j in range(1, n):
        S[j] = max(r[perm[j]], C[j-1])
        C[j] = S[j] + p[perm[j]]
        Cmax = max(Cmax, C[j] + q[perm[j]])
        harm[j]=[S[j],C[j],C[j]+q[j]]
    print(f"harm = {harm}")
    return Cmax

def main():
    seed = 1
    x=29
    rng = RandomNumberGenerator(seed)
    n = 12 # liczba zadan
    p = []
    for _ in range(1, n+1):
        p.append(rng.nextInt(1, 29))
    print("p =", p)
    A = sum(p)

    r = []
    for _ in range(1, n+1):
        r.append(rng.nextInt(1, A))
    print("r = ", r)

    q = []
    for _ in range(1, n+1):
        q.append(rng.nextInt(1, A))
    print("q =", q)

    pi = [i for i in range(0, n)]
    print("pi =", pi)
    
    
    Cmax = calculate(pi, r, p, q)
    
    print(f"Cmax = {Cmax}")

if __name__ == "__main__":
    main()
