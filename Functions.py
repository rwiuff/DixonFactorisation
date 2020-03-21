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
