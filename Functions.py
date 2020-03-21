import numpy as np


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def Factorbase(n):
    if n < 2:
        print("No primes in this base")
    base = np.array([-1])
    interval = np.arange(2, n + 1, 1)
    for i in range(interval.size):
        if is_prime(interval[i]) is True:
            base = np.append(base, interval[i])
    return base


def ExponentVector(n, b):
    EV = np.zeros(b.size)
    if n % b[0] == 0:
        EV[0] = 1
    for i in range(1, b.size):
        if n % b[i] == 0:
            EV[i] = 1
            j = 0
            while n % b[i]**j == 0:
                j = j + 1
                EV[i] = j - 1
        else:
            EV[i] = 0
    return EV
