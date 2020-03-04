import time
def fib1(n):
    if n>1:
        return fib1(n-1) + fib1(n-2)
    elif n==1:
        return 1
    else:
        return 0
def fib2(n):
    wynik1=0
    wynik2=1
    for i in range(1, n+1):
        wynik1,wynik2 = wynik2, wynik2 + wynik1
    return wynik2
def zmierz(f, n=100):
    t0=time.time()
    w=f(n)
    t1=time.time()
    return t1-t0
czas1= zmierz(fib1)
czas2= zmierz(fib2)
print(czas1)
print(czas2)
