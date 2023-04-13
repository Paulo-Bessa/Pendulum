import sys
import numpy as np
from lorenz import *
from runge_kutta import *
from numpy.linalg import norm,qr
from gram import gs
import matplotlib.pyplot as plt
from distance import dist

tmax = 2
t0 = 0
step = 1e-2
thrsh = 15
init = np.ones(3)
ancient_eta = np.eye(3)

lam1 = [1]
lam2 = [1]
lam3 = [1]

time_r, ref = runge_kutta_integrator(lorenz,init,t0,tmax,step)        
ans_ref = ref.T
eps = ancient_eta
for i in range(1,int(tmax/step)):
    x = ans_ref[i]
    eta = np.exp(lin_lorenz(x,t0)*t0)
    pre_eps = x + eta

    _,opa,_ = np.linalg.svd(eta)
    print("SE LIGA "+str(opa))

    # print("A trajetoria de referencia eh "+str(x)+" e a perturbada eh "+str(pre_eps)+"\n")
    t0+=step
    aval1 = dist(pre_eps[0],x)
    aval2 = dist(pre_eps[1],x)
    aval3 = dist(pre_eps[2],x)

    # print("Aval1 eh: "+str(aval1))
    # print("Aval2 eh: "+str(aval2))
    # print("Aval3 eh: "+str(aval3)+"\n")

    # print("Aqui o lam 1: "+str(lam1)+"\n")
    dists = [aval1,aval2,aval3]
    # print("As distancias sao: "+str(dists))
    if max(dists) >= thrsh:
        # print("Dentro do log vai "+str(aval1))
        # print("O t0 eh: "+str(t0))
        lam1.append((np.log(aval1)+lam1[-1])/t0)
        lam2.append((np.log(aval2)+lam2[-1])/t0)
        lam3.append((np.log(aval3)+lam3[-1])/t0)
        # print("PAUSA\n")
        eta=gs(pre_eps)

print("Os lambdas finais sao: "+str(lam1[-1])+", "+str(lam2[-1])+" e "+str(lam3[-1]))

# for elem in lam3:#np.arange(0,2000,50):
#     print("Espectro3 eh "+str(elem))
    # print("Espectro2 eh "+str(lam2[elem]))
    # print("Espectro3 eh "+str(lam3[elem]))
# plt.plot(range(len(lam1[300:])),lam1[300:])
# plt.plot(range(len(lam2[300:])),lam2[300:])
# plt.plot(range(len(lam3[300:])),lam3[300:])
# plt.show()