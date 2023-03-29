from RandomNumberGenerator import *  # importowanie modułu generującego liczby losowe
import numpy as np  # importowanie modułu do obsługi macierzy i tablic
import math  # importowanie modułu matematycznego
import random  # importowanie modułu do obsługi funkcji losowych


def schrage(perm, r, p, q):
    n = len(perm)  # liczba zadań
    N = []  # zbiór zadań nieuszeregowanych
    G = []  # zbiór zadań gotowych do realizacji
    pi = []  # kolejność realizacji zadań

    for i in range(n):
        N.append(i)  # każde zadanie zaczyna w zbiorze N

    t = min(r)  # czas startu

    # Główna pętla algorytmu
    while G or N:
        while N and min(r[i] for i in N) <= t:
            j = N[np.argmin([r[i] for i in N])]  # wybierz zadanie o najmniejszym czasie dostępności
            G.append(j)  # dodaj wybrane zadanie do zbioru zadań gotowych
            N.remove(j)  # usuń wybrane zadanie ze zbioru nieuszeregowanych

        if G:  # jeśli brak zadań gotowych
            j = G[np.argmax([q[i] for i in G])]  # wybierz zadanie o największym czasie stygnięcia
            G.remove(j)  # usuń wybrane zadanie ze zbioru zadań gotowych
            pi.append(j)  # dodaj wybrane zadanie do kolejności realizacji
            t += p[j]  # zaktualizuj czas
        else:
            t = min(r[i] for i in N)  # przesuń czas startu do najbliższego czasu dostępności zadania

    return pi


def calculate(pi, r, p, q):
    n = len(pi)  # liczba zadań
    S = [0]*n  # czas rozpoczęcia każdego zadania
    C = [0]*n  # czas zakończenia każdego zadania
    harm=[0]*n
    Cmax = 0  # wartość funkcji celu - maksymalny czas trwania procesu

    # Obliczanie wartości funkc0i celu
    S[0] = r[pi[0]]
    C[0] = S[0] + p[pi[0]]
    Cmax = C[0] + q[pi[0]]
    harm[0]=[S[0],C[0],C[0]+q[0]]
    for j in range(1, n):
        S[j] = max(r[pi[j]], C[j-1])
        C[j] = S[j] + p[pi[j]]
        Cmax = max(Cmax, C[j] + q[pi[j]])
        harm[j]=[S[j],C[j],C[j]+q[j]]
    print(f"harm = {harm}")
    return Cmax


def main():
    rng = RandomNumberGenerator(1)
    n=12
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

    
    pi = schrage(pi, r, p, q)
    
    
    Cmax = calculate(pi, r, p, q)
    for i in range(0,n):
        pi[i]=pi[i]+1
         
    print(f"Kolejnosc: {pi}")
    print(f"Cmax = {Cmax}")

if __name__ == "__main__":
    main()
