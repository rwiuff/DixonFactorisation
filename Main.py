from Functions import Factorbase, ExponentVector
from math import gcd

N = 84923

B = 19

P = Factorbase(B)
print(P)
Q = -2394
EV = ExponentVector(Q, P)
print(EV)
