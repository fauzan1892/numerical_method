import numpy as np
import matplotlib.pyplot as plt
from math import e
# mendefinisikan fungsi
def f(x):
    return e**x-8*x**2
#mendefinisikan turunan fungsi
def Df(x):
    return e**x-16*x

# metode newton raphson
def newtonRaphson(x0,eps):
    step = 0
    print('\n\n*** -- Metode Newton Raphson -- ***')
    xn = x0
    for n in range(0,100):
      fxn = f(xn) 
      if abs(fxn) < eps:
        print('\n Akar Persamaan tersebut : %0.8f' % xn)
        return xn
      Dfxn = Df(xn)
      if Dfxn == 0:
        print('Solusi tidak ditemukan')
        return None
      xn=xn-(fxn/Dfxn)
      step = step+1
      print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
    print('Iterasi maksimum, solusi tidak ditemukan')


x0 = float(input('x0: '))
eps = float(input('epsilon : '))
newtonRaphson(x0,eps)
