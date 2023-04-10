import numpy as np

def henon_step(x,y,a=1.4,b=0.3):
    """One step of the Henon map"""
    xnew=a-x*x+b*y
    ynew=x
    return (xnew,ynew)

def henon_map(x,y,ns=1e4,a=1.4,b=0.3):
    """"Henon map with standard configuration a=1.4,
     b=0.3 and number of points 10.000"""
    xs=[x]
    ys=[y]
    for _ in range(int(ns)):
        x,y = henon_step(xs[-1],ys[-1])

        xs.append(x)
        ys.append(y)
    return (xs,ys)

def Jacobian_henon(point,a=1.4,b=0.3):
    """Returns the Jacobian matrix of the Henon map
    with standard parameters a=1.4 and b=0.3."""
    return np.array([[-2*point[0], b],[1,0]])

def DF_Dparameter(point,a=1.4,b=0.3):
    """Returns the vector w, that is the Derivative
    of the dynamical system using the parameter a as variable."""
    return np.array([[1],[0]])

def DF_Dparameters(point,a=1.4,b=0.3):
    """Returns the vector w, that is the Derivative
    of the dynamical system using the parameter a and b
    as variables."""
    return np.array([[1,point[1]],[0,0]])