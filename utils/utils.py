# coding: utf-8


# Librairies
from math import *
from numpy import random, sqrt, log, sin, cos, pi, fabs, exp
import numpy as np


def gauss1(mu_x=0, sigma_x=1, nb_sim=1):
    return np.random.normal(mu_x, sigma_x, nb_sim)


def gauss2():
    # uniformly distributed values between 0 and 1
    u1 = random.rand(1)  # random.rand(1000)
    u2 = random.rand(1)
    z1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
    # z2 = sqrt(-2 * log(u1)) * sin(2 * pi * u2)
    return z1  # z2


def phi(x):
    # Cumulative distribution function for the standard normal distribution
    # math.erf(x) returns the error function at x.
    return (1.0 + erf(x / sqrt(2.0))) / 2.0


def N(X):
    a1 = 0.31938153
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429

    L = fabs(X)
    K = 1 / (1 + 0.2316419 * L)
    res = 1 - 1 / sqrt(2 * pi) * exp(-L ^ 2 / 2) * (a1 * K + a2 * K ^ 2 + a3 * K ^ 3 + a4 * K ^ 4 + a5 * K ^ 5)

    if X < 0:
        res = 1 - res

    return res


def pgaussred(x):
    """fonction de répartition de la loi normale centrée réduite
       (= probabilité qu'une variable aléatoire distribuée selon
       cette loi soit inférieure à x)
       calcul par intégration numérique: 2000 tranches par écart-type
       résultat arrondi à 7 chiffres après la virgule
    """
    if x==0:
        return 0.5
    u=abs(x)
    n=int(u*2000)
    du=u/n
    k=1/sqrt(2*pi)
    u1=0
    f1=k
    p=0.5
    for i in range(0,n):
        u2=u1+du
        f2=k*exp(-0.5*u2*u2)
        p=p+(f1+f2)*du*0.5
        u1=u2
        f1=f2
    if x<0:
        p = 1.0-p
    return round(p, 7)


def pgaussred(x):
    """fonction de répartition de la loi normale centrée réduite
       (= probabilité qu'une variable aléatoire distribuée selon
       cette loi soit inférieure à x)
       formule simplifiée proposée par Abramovitz & Stegun dans le livre
       "Handbook of Mathematical Functions" (erreur < 7.5e-8)
    """
    u = abs(x)  # car la formule n'est valable que pour x>=0

    Z = 1 / (sqrt(2 * pi)) * exp(-u * u / 2)  # ordonnée de la LNCR pour l'absisse u

    b1 = 0.319381530
    b2 = -0.356563782
    b3 = 1.781477937
    b4 = -1.821255978
    b5 = 1.330274429

    t = 1 / (1 + 0.2316419 * u)
    t2 = t * t
    t4 = t2 * t2

    P = 1 - Z * (b1 * t + b2 * t2 + b3 * t2 * t + b4 * t4 + b5 * t4 * t)

    if x < 0:
        P = 1.0 - P  # traitement des valeurs x<0

    return round(P, 7)  # retourne une valeur arrondie à 7 chiffres