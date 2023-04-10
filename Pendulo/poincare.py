import numpy as np

def poincare_section(ans,time,freq,tol=1e-2,eps=0):
    points = []
    ans=np.array(ans)
    for i in range(len(time)):
        if (time[i]+eps)%(2*np.pi*freq)<tol:
            points.append((ans.T)[i])
    return np.array(points)