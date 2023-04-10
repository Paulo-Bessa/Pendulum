import numpy as np

def lorenz(x,t,sigma=16,R=45.92,b=4):
    x1 = sigma*(x[1]-x[0])
    x2 = x[0]*(R-x[2])-x[1]
    x3 = x[0]*x[1] - b*x[2]
    x11 = -sigma
    x12 = sigma
    x13 = 0
    x21 = R-x[2]
    x22 = -1
    x23 = -x[0]
    x31 = x[1]
    x32 = x[0]
    x33 = -b
    return np.array([x1,x2,x3,x11,x12,x13,x21,x22,x23,x31,x32,x33])

def lin_lorenz(x,t,sigma=16,R=45.92,b=4):
    x11 = -sigma
    x12 = sigma
    x13 = 0
    x21 = R-x[2]
    x22 = -1
    x23 = -x[0]
    x31 = x[1]
    x32 = x[0]
    x33 = -b
    return np.array([[x11,x12,x13],
                     [x21,x22,x23],
                     [x31,x32,x33]])
