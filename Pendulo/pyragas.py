from rungekutta import runge_kutta_4_step
import numpy as np
from params import Args
from pendulo import model

def pyrag_gain(K,State,old_State):
    Ft = K*(old_State[1]-State[1])
    return Ft

def pyrag(K,period,y0,t0,tmax,h):
    ts   = np.array([t0])
    ys   = np.array([y0])
    count=0
    while (t0<tmax):
        if count>period:
            F = pyrag_gain(K, y0, ys[-period])
            f = lambda x,t: model(x,t,Args,F)
            (y0,t0) = runge_kutta_4_step(f,y0,t0,h)
            ts = np.append(ts,t0)
            ys = np.concatenate((ys,np.array([y0])))
        else:
            f = lambda x,t: model(x,t,Args)
            (y0,t0) = runge_kutta_4_step(f,y0,t0,h)
            ts = np.append(ts,t0)
            ys = np.concatenate((ys,np.array([y0])))
        count+=1
    ys = ys.T
    return [ts,ys]
