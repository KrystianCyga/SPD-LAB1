from RandomNumberGenerator import *  # importowanie modułu generującego liczby losowe
import numpy as np  # importowanie modułu do obsługi macierzy i tablic


def shrage_z_przerwaniami(perm, r, p, q):
    n = len(perm)  # liczba zadań
    N = []  # zbiór zadań nieuszeregowanych
    G = []  # zbiór zadań gotowych do realizacji
    pi = []  # kolejność realizacji zadań
    l = 0 #ostatnie wykonane zadanie

    for i in range(n):
        N.append(i)  # każde zadanie zaczyna w zbiorze N

    t = min(r)  # czas startu
    Cmax = 0  # maksymalny czas zakończenia zadań

    while G or N:
        while N and min(r[i] for i in N) <= t:
            j = N[np.argmin([r[i] for i in N])]  # wybierz zadanie o najmniejszym czasie dostępności
            G.append(j)  # dodaj wybrane zadanie do zbioru zadań gotowych
            N.remove(j)  # usuń wybrane zadanie ze zbioru nieuszeregowanych

            if q[j] > q[l]:  # przerwanie zadania aktualnie wykonywanego jesli dostepne z wiekszym q
                p[l] = t - r[j]  # oblicz czas dowykonywania przerwanego zadania
                t = r[j]  # przesuń czas startu do czasu dostępności zadania z wiekszym q
                if p[l] > 0:
                    G.append(l)  # dodaj przerwane zadanie do zbioru zadań gotowych
        if G:# jeśli są zadania gotowe
            j = G[np.argmax([q[i] for i in G])]  # wybierz zadanie o największym czasie stygnięcia
            G.remove(j)  # usuń wybrane zadanie ze zbioru zadań gotowych
            pi.append(j)  # dodaj wybrane zadanie do kolejności realizacji
            l = j; #podmien aktualne zadanie
            t += p[j]  # zaktualizuj czas
            Cmax = max(Cmax, t + q[j]) # znajdz najwieksze Cmax
        else:
            t = min(r[i] for i in N)  # przesuń czas startu do najbliższego czasu dostępności zadania

    return pi, Cmax




def main():
    rng = RandomNumberGenerator(1)

    p = []
    for _ in range(1, 13):
        p.append(rng.nextInt(1, 29))
    print("p =", p)
    A = sum(p)

    r = []
    for _ in range(1, 13):
        r.append(rng.nextInt(1, A))
    print("r = ", r)

    q = []
    for _ in range(1, 13):
        q.append(rng.nextInt(1, A))
    print("q =", q)

    pi = [i for i in range(1, 13)]
    print("pi =", pi)

    pi, cmax = shrage_z_przerwaniami(pi, r, p, q)
    print(f"Kolejnosc: {pi}")

    print(f"Cmax = {cmax}")


if __name__ == "__main__":
    main()
