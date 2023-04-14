import numpy as np

# Um passo do método Runge Kutta de ordem 4
def runge_kutta_4_step(f,y0,t0,h):
    #y0 = np.array(y0)
    
    k1 = f(y0,t0)
    k2 = f(y0 + (h/2)*k1, t0 + h/2)
    k3 = f(y0 + (h/2)*k2, t0 + h/2)
    k4 = f(y0 + h*k3, t0 + h)

    y0 = y0 + h*(k1 + 2*k2 + 2*k3 + k4)/6
    t0 = t0 + h
        
    return [y0,t0]

def rg4(f,y0,t0,h,tmax):
    ts   = np.array([t0])
    ys   = np.array([y0])
    
    l1=False
    l2=False
    l3=False
    l4=False
    l5=False
    l6=False
    l7=False
    l8=False
    l9=False
    l10=False
    l11=False
    l12=False
    l13=False
    l14=False
    l15=False
    l16=False
    l17=False
    l18=False
    l19=False
    l20=False
    while (t0<tmax):
        if t0/tmax > 0.05 and not l1:
            print("5% concluido")
            l1=True
        if t0/tmax > 0.1 and not l2:
            print("10% concluido")
            l2=True
        if t0/tmax > 0.15 and not l3:
            print("15% concluido")
            l3=True
        if t0/tmax > 0.2 and not l4:
            print("20% concluido")
            l4=True
        if t0/tmax > 0.25 and not l5:
            print("25% concluido")
            l5=True
        if t0/tmax > 0.3 and not l6:
            print("30% concluido")
            l6=True
        if t0/tmax > 0.35 and not l7:
            print("35% concluido")
            l7=True
        if t0/tmax > 0.4 and not l8:
            print("40% concluido")
            l8=True
        if t0/tmax > 0.45 and not l9:
            print("45% concluido")
            l9=True
        if t0/tmax > 0.5 and not l10:
            print("50% concluido")
            l10=True
        if t0/tmax > 0.55 and not l11:
            print("55% concluido")
            l11=True
        if t0/tmax > 0.6 and not l12:
            print("60% concluido")
            l12=True
        if t0/tmax > 0.65 and not l13:
            print("65% concluido")
            l13=True
        if t0/tmax > 0.7 and not l14:
            print("70% concluido")
            l14=True
        if t0/tmax > 0.75 and not l15:
            print("75% concluido")
            l15=True
        if t0/tmax > 0.8 and not l16:
            print("80% concluido")
            l16=True
        if t0/tmax > 0.85 and not l17:
            print("85% concluido")
            l17=True
        if t0/tmax > 0.9 and not l18:
            print("90% concluido")
            l18=True
        if t0/tmax > 0.95 and not l19:
            print("95% concluido")
            l19=True
        if t0/tmax > 0.99 and not l20:
            print("99% concluido")
            l20=True
        (y0,t0) = runge_kutta_4_step(f,y0,t0,h)
        ts = np.append(ts,t0)
        ys = np.concatenate((ys,np.array([y0])))
    ys = ys.T

    return [ts,ys]