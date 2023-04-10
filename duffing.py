import numpy as np


def duf_osc(x,t, alpha=0.05, gamma=-0.2, beta=1, Omega=1, mu=7.5):
    return np.array([x[1], -alpha*x[1] - gamma*x[0] - beta*x[0]*x[0]*x[0] + mu*np.sin(Omega*t)])

def Jacobian_duf(x,t, alpha=0.05, gamma=-0.2, beta=1, Omega=1, mu=7.5):
    x11 = 0
    x12 = 1
    x21 = -gamma - 2 * beta * x[0]* x[0]
    x22 = -alpha
    return np.array([[x11,x12],[x21,x22]])

def DF_Dparameter(x,t, alpha=0.05, gamma=-0.2, beta=1, Omega=1, mu=7.5):
    """Returns the vector w, that is the Derivative
    of the dynamical system using the parameter a as variable."""
    return np.array([0,np.cos(Omega*t)])

def DF_sc(x,t, alpha=0.05, gamma=-0.2, beta=1, Omega=1, mu=7.5):
    """Returns the matrix Wn, that is the Derivative
    of the dynamical system using all the parameters."""
    Wn = np.array([[0,0,0,0,0],
                   [x[1],x[0],x[0]*x[0]*x[0],np.sin(Omega*t),mu*np.cos(Omega*t)]])
    return Wn