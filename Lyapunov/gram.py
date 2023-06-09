import numpy as np
from numpy.linalg import norm

def gs_cofficient(v1, v2):
    return np.dot(v2, v1) / np.dot(v1, v1)

def multiply(cofficient, v):
    return map((lambda x : x * cofficient), v)

def proj(v1, v2):
    return multiply(gs_cofficient(v1, v2) , v1)

def gs(X):
    Y = []
    for i in range(len(X)):
        temp_vec = X[i]
        for inY in Y :
            proj_vec = proj(inY, X[i])
            #print "i =", i, ", projection vector =", proj_vec
            temp_vec = list(map(lambda x, y : x - y, temp_vec, proj_vec))
            #print "i =", i, ", temporary vector =", temp_vec
        Y.append(temp_vec)
    for i,elem in enumerate(Y):
        Y[i] = elem/norm(elem)
    return np.array(Y)
