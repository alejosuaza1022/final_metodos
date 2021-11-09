from sympy import *
import math
import numpy as np


x = Symbol('x')
y = Symbol('y')
fun = vars(math)


def superior(x, y, f, h, xi, xf):
    n = int((xf-xi)/h)
    xsol = [x]
    ysol = [y]
    for i in range(n):
        k1 = eval(f, fun, {"x": x, "y": y})
        k2 = eval(f, fun, {"x": x + (1/4) * h, "y": y+(1/4)*k1*h})
        k3 = eval(f, fun, {"x": x + (1/4) * h, "y": y+(1/8)*k1*h + (1/8)*k2*h})
        k4 = eval(f, fun, {"x": x + (1/2) * h, "y": y - (1/2)*k2*h + k3*h})
        k5 = eval(f, fun, {"x": x + (3/4)*h,
                  "y": y - (3/16)*k1*h + (9/16)*k4*h})
        k6 = eval(f, fun, {"x": x + h, "y": y - (3/7)
                  * k1*h + (12/7)*k3*h + (8/7)*k5*h})
        xn = x + h
        yn = y + (1/90)*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*h
        xsol.append(xn)
        ysol.append(yn)
        x = xn
        y = yn

    return xsol, ysol


def rk4(x, y, f, h, xi, xf):
    n = int((xf-xi)/h)
    xsol = [x]
    ysol = [y]
    for i in range(n):
        k1 = eval(f, fun, {"x": x, "y": y})
        k2 = eval(f, fun, {"x": x + (1/2)*h, "y": y+(1/2)*k1*h})
        k3 = eval(f, fun, {"x": x + (1/2)*h, "y": y+(1/2)*k2*h})
        k4 = eval(f, fun, {"x": x+h, "y": y+k3*h})
        xn = x + h
        yn = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h
        xsol.append(xn)
        ysol.append(yn)
        x = xn
        y = yn

    return xsol, ysol


def regresion_lineal(x, y):
    n = x.shape[0]
    sumxy = 0
    sumx = 0
    sumy = 0
    sumx2 = 0
    for a, b in zip(x, y):
        sumxy += a*b
        sumx += a
        sumy += b
        sumx2 += a**2

    sumx2den = sumx**2
    mediax = sumx/n
    mediay = sumy/n

    a1 = ((n*sumxy) - (sumx*sumy)) / ((n * sumx2) - (sumx2den))
    a0 = (mediay - (a1*mediax))

    yest = a0 + a1*x

    return a0, a1, yest


def ajuste(y, yest):
    sumy = sum(b for b in y)
    mediay = sumy/y.shape[0]
    Sr = 0
    St = 0
    for i, yt in zip(y, yest):
        St += (i-mediay)**2
        Sr += (i-yt)**2

    R2 = (St-Sr)/St
    R = np.sqrt(R2)

    return R2, R


def modelo_regresion(x, y):
    x = np.array(x, np.float)
    y = np.array(y, np.float)
    intercepto, pendiente, yest = regresion_lineal(x, y)
    _, CoefCorr = ajuste(y, yest)
    return CoefCorr, intercepto, pendiente, yest


    

