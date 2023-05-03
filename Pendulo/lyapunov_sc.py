import numpy as np
import matplotlib.pyplot as plt

def sys(x,t):
    x1,x2,x3,x4,x5,x6=x
    F = K*((1-R)*())

    dx1=x2
    dx2= -(k*d*d*x1)/(2*I) - xi*x2/I + (k*d*deltaf)/(2*I) - m*g*D*np.sin(x1)/(2*I) - 2*mu*np.arctan(1e6*x2) + F