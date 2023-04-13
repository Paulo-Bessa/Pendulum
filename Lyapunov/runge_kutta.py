import numpy as np 

def rk4_step(f,y0,t0,h=1e-3):
    """Step of the Runge-Kutta integrator of function f.
     Outputs (y,t)"""
    y0=np.array(y0)
    k1 = f(y0,t0)
    k2 = f(y0 + (h/2)*k1, t0 + h/2)
    k3 = f(y0 + (h/2)*k2, t0 + h/2,)
    k4 = f(y0 + h*k3, t0 + h)

    y0 = y0 + h*(k1 + 2*k2 + 2*k3 + k4)/6
    t0 = t0 + h
        
    return (y0,t0)

def runge_kutta_integrator(f,y,t0,tmax,step=1e-3,activator=False):
    """Runge-Kutta integrator of function f from time t0
    to time tmax with standard step size of 1e-3."""
    ts   = np.array([t0])
    ys   = np.array([y])

    while (t0<tmax):
        (y,t0) = rk4_step(f,y,t0,step)
        if activator:
            arch = open('New_doc.csv','a')
            arch.write(str(y[0])+","+str(y[1])+","+str(t0)+'\n') #Give your csv text here.
            ## Python will convert \n to os.linesep
            arch.close()
        ts = np.append(ts,t0)
        ys = np.concatenate((ys,np.array([y])))
    return (ts,ys.T)
